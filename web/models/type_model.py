"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

import datetime
from . import db


class TypeModel(db.Model):

    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    note = db.Column(db.String(), nullable=True)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    device = db.relationship('DeviceModel', backref='device', lazy=True)

    def __init__(self, id, name, description, note):
        self.id = id
        self.name = name
        self.description = description
        self.note = note
        self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return TypeModel.query.all()

    @staticmethod
    def get(id):
        return TypeModel.query.get(id)

    @staticmethod
    def get_by_name(name):
        return TypeModel.query.filter_by(name=name).first()

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'note': self.note,
            'created': self.created,
            'modified': self.modified
        }
