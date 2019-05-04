"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from datetime import datetime

from . import db, TableName


class DeviceStatus(db.Model):
    __tablename__ = TableName.DEVICE_STATUS

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.String(255), unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    def __int__(self):
        pass

    def __init__(self, device_id, value, time):
        self.device_id = device_id
        self.value = value
        self.time = time

    def __repr__(self):
        return 'id: {}, device_id: {}, value: {}, time: {}'.format(self.id, self.device_id, self.value, self.time)

    def insert(self):
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
        return DeviceStatus.query.all()

    @staticmethod
    def get_by_id(id):
        return DeviceStatus.query.get(id)

    @staticmethod
    def get_by_device_id(id):
        return DeviceStatus.query.filter_by(device_id=id).all()

    def serialize(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'value': self.value,
            'time': self.time
        }
