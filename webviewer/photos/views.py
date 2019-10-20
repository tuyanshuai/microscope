# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from webviewer.photos.models import Photo
from flask_paginate import Pagination, get_page_args


blueprint = Blueprint("photos", __name__, url_prefix="/photos", static_folder="/static", static_url_path='/static')


@blueprint.route("/")
@blueprint.route("/<int:page>/")
@login_required
def index(page = 1):
    """List Photos."""

    per_page = 6
    photos = Photo.query.all()
    total = len(photos)
    pagination_photos = Photo.query.order_by(Photo.photo_id.desc()).paginate(page, per_page, error_out=False).items

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("public/photos.html",
                           photos=pagination_photos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination )
