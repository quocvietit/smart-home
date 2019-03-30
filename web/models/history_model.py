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


class HistoryModel(db.Model):

    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text(), nullable=False)
    time = db.Column(db.DateTime)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    def __init__(self, id, name, description, note):
        self.id = id
        self.name = name

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
    def get_all_device():
        return HistoryModel.query.all()

    @staticmethod
    def get_device(id):
        return HistoryModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id
        }
