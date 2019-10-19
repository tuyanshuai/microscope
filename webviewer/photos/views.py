# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("photos", __name__, url_prefix="/photos", static_folder="../static")


@blueprint.route("/")
@login_required
def home():
    """List Photos."""
    return render_template("public/photos.html")    # we may modify to user owned image
