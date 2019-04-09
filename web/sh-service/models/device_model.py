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


class DeviceModel(db.Model):

    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    last_activity = db.Column(db.DateTime, nullable=True)
    is_connect = db.Column(db.Boolean, nullable=False, default=False)
    is_enable = db.Column(db.Boolean, nullable=False, default=False)

    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)

    history = db.relationship('HistoryModel', backref='history', lazy=True)

    def __init__(self, data):
        self.name = data.get('name')
        self.last_activity = data.get('last_activity')
        self.is_connect = data.get('is_connect')
        self.is_enable = data.get('is_enable')

    def __repr__(self):
        return '<id {}>'.format(self.id)

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
        return DeviceModel.query.all()

    @staticmethod
    def get(id):
        return DeviceModel.query.get(id)

    @staticmethod
    def get_by_type(type_id):
        return DeviceModel.query.filter_by(type_id=type_id).first()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_activity': self.last_activity,
            'is_connect': self.is_connect,
            'is_enable': self.is_enable
        }
