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
from webviewer.extensions import (
    db
)

blueprint = Blueprint('virtual_cam', __name__, static_folder="static", static_url_path='/virtual_cam/static')

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')



@blueprint.route('/camera', methods=['GET', 'POST'])
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

        print("action=%s"%action)

        print("request.data=%s"%request.data)

        if action == "snap":
            url_path = "/virtual_cam/static/%d.jpg" % time.time()
            img_path = os.path.join(script_dir, "../"+url_path)
            print (img_path)
            fake_image.save(img_path) # save image
            # update database
            photo = Photo(photo_path=url_path)
            db.session.add(photo)
            db.session.commit()
            retmsg = "Image %s is saved"%url_path
            return retmsg, 200

        return "unknow action", 200




