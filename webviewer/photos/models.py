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

class Photo(Model):
    """ The photo/picture mode"""
    __tablename__ = "photos"
    photo_id = Column(db.Integer, unique = True, primary_key = True)
    photo_path = Column(db.String(2048), unique=True,  nullable=False)    
    owner_id =  relationship("User", backref="photos")  # refer to the user_id

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Photo({id},{path})>".format(id=self.photo_id, path=self.photo_path)
 
