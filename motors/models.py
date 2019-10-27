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


class Motors(Model):
    """ The photo/picture mode"""
    __tablename__ = "Motors"
    id = Column(db.Integer, primary_key = True)
    x = Column(db.DECIMAL)
    y = Column(db.DECIMAL)
    z = Column(db.DECIMAL)
    xlim = Column(db.DECIMAL)
    ylim = Column(db.DECIMAL)
    zlim = Column(db.DECIMAL)
    status = Column(db.Integer)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,  **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Motors({status})>".format(id=self.status)

