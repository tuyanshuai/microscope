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

class ScanConfig(Model): 
    __tablename__ = "ScanConfig"
    id = Column(db.Integer, primary_key =True) 

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,  **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<ScanConfig>"

class AutoRun(Model):
    """ AutoRun Table"""
    __tablename__ = "AutoRun"
    id = Column(db.Integer, primary_key =True )  # auto increase
    x =  Column(db.Decimal)  # 
    y =  Column(db.Decimal)  #  
    z =  Column(db.Decimal)  # 
    action = Column(db.String)  #     

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,  **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<ScanConfig>"