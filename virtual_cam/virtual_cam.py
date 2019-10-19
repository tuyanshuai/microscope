# -*- coding: utf-8 -*-
"""The app module, containing the app factory function, is used to serve as fake camera"""
import logging
import sys

from flask import Flask, render_template, request, Blueprint, send_file
from io import BytesIO
from PIL import Image
import time, math, os

blueprint = Blueprint('cam', __name__)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')



@blueprint.route('/image')
def image():
    # qvalue = request.form['q'] # will not use now

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "../virtual_cam/image.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    im = Image.open(abs_file_path)
    im = im.rotate(math.fmod(time.time()*5,360))
    time.sleep(0.1)
    return serve_pil_image(im)


@blueprint.route("/")
def home():
    return 'home'

@blueprint.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r