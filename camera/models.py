# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from webviewer.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)


class Camera(Model):
    """ The photo/picture mode"""
    __tablename__ = "Camera"
    camera_id = Column(db.Integer, unique=True, primary_key=True)
    camera_exposure = Column(db.Integer)
    camera_gain = Column(db.Integer)
    camera_status = Column(db.Integer)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,  **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Camera({id})>".format(id=self.camera_id)

