# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from webviewer.photos.models import Photo
from flask_paginate import Pagination, get_page_args


blueprint = Blueprint("photos", __name__, url_prefix="/photos", static_folder="../static")

users = list(range(100))
def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]

@blueprint.route("/")
@blueprint.route("/<int:page>/")
@login_required
def index(page = 1):
    """List Photos."""


    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("public/photos.html",
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination )

    # photos_per_page = 4
    # photos=[{'href': "https://mdbootstrap.com/img/Photos/Lightbox/Original/img%20(145).jpg", 'src': "https://mdbootstrap.com/img/Photos/Lightbox/Thumbnail/img%20(145).jpg"},
    #         {'href': "https://mdbootstrap.com/img/Photos/Lightbox/Original/img%20(150).jpg", 'src': "https://mdbootstrap.com/img/Photos/Lightbox/Thumbnail/img%20(150).jpg"},
    #         {'href': "https://mdbootstrap.com/img/Photos/Lightbox/Original/img%20(152).jpg", 'src': "https://mdbootstrap.com/img/Photos/Lightbox/Thumbnail/img%20(152).jpg"},
    #         {'href': "https://mdbootstrap.com/img/Photos/Lightbox/Original/img%20(42).jpg", 'src': "https://mdbootstrap.com/img/Photos/Lightbox/Thumbnail/img%20(42).jpg"}]
    #
    #
    # photos = Photo.query.order_by(Photo.photo_id).paginate(page, photos_per_page, error_out=False)
    # return render_template("public/photos.html", photos =photos)    # we may modify to user owned image
