# -*- coding: utf-8 -*-
"""The app module, containing the app factory function, is used to serve as fake camera"""
import logging
import sys

from flask import Flask, render_template, request, Blueprint, send_file
from flask import flash
from io import BytesIO
from PIL import Image
import time, math, os
from webviewer.photos.models import Photo
from camera.models import Camera
from webviewer.extensions import (
    db
)

import json


blueprint = Blueprint('camera', __name__, url_prefix="/camera", static_folder="static", static_url_path='/camera/static')

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@blueprint.route('/image', methods=['GET', 'POST'])
def image():

    # Generate fake image
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "image.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    im = Image.open(abs_file_path)
    fake_image = im.rotate(math.fmod(time.time() * 5, 360))
    if request.method == 'GET':
        return serve_pil_image(fake_image)
    else:
        print("take an action")
        action = request.args.get('action', '')
        action_para = request.args.get('parameters', '')

        print("action=%s"%action)

        print("request.data=%s"%request.data)

        if action == "snap":
            img_url_path = "../camera/static/%d.jpg" % time.time()
            img_path = os.path.join(script_dir, "../"+img_url_path)
            print (img_path)
            fake_image.save(img_path) # save image
            # update database
            photo = Photo(photo_path=img_url_path)
            db.session.add(photo)
            db.session.commit()
            return_msg = "Image %s is saved"%img_url_path
            return return_msg, 200

        return "Unknown action", 200



@blueprint.route('/set', methods=['POST'])
def set_camera():
    action = request.args.get('action', '')
    action_para = request.args.get('parameters', '')

    print("action=%s, parameters=%s"%(action, action_para))

    if action == "open":
        return "Camera is opened", 200

    if action == "close":
        return "Camera is closed", 200

    if action == "startCapture":
        return "Camera is capturing", 200

    if action == "stopCapture":
        return "Camera  stop capture", 200

    if action == "setPara":
        para_dict = json.loads(action_para)
        print(para_dict)
        cam = Camera.query.first()

        if cam is None:
            cam = Camera()
            db.session.add(cam)
            db.session.commit()
            cam = Camera.query.first()


        cam.camera_exposure = para_dict["exposure"]
        cam.camera_gain = para_dict["gain"]
        db.session.commit()

        cam_para = {"id": cam.camera_id,
                    "exposure": cam.camera_exposure,
                    "gain": cam.camera_gain,
                    "status": cam.camera_status}
        return "Camera parameres as %s "% json.dumps(cam_para), 200

    if action == "getPara":
        cam = Camera.query.first()

        if cam is None:
            cam = Camera()
            db.session.add(cam)
            db.session.commit()
            cam = Camera.query.first()


        cam_para = {"id": cam.camera_id,
                    "exposure": cam.camera_exposure,
                    "gain": cam.camera_gain,
                    "status": cam.camera_status}

        return json.dumps(cam_para), 200

    # image = getImage(resolution, quality)
    # 1.    resolution = Small        Normal        Large
    # 2.        quality        Jpeg压缩比
    # 8.    getFocusNum(rio, scale)
    return "Unknown action", 200




