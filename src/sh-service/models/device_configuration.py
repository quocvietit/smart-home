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


class DeviceConfiguration(db.Model):
    __tablename__ = TableName.DEVICE_CONFIGURATION

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    key = db.Column(db.String(255), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)
    modified = db.Column(db.DateTime, nullable=False)

    device_type_id = db.Column(db.Integer, db.ForeignKey('device_type.id'), nullable=False)

    def __int__(self):
        pass

    def __init__(self, type_id, key, value):
        self.device_type_id = type_id
        self.key = key
        self.value = value
        self.modified = datetime.now()

    def __repr__(self):
        return 'id: {}, device_type_id: {}, key: {}, value: {}, modified: {}'.format(self.id, self.device_type_id,
                                                                                     self.key, self.value,
                                                                                     self.modified)

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
        return DeviceConfiguration.query.all()

    @staticmethod
    def get_by_id(id):
        return DeviceConfiguration.query.get(id)

    @staticmethod
    def get_by_device_type_id(id):
        return DeviceConfiguration.query.filter_by(device_type_id=id).all()

    def serialize(self):
        return {
            'id': self.id,
            'device_type_id': self.device_type_id,
            'key': self.key,
            'value': self.value,
            'modified': self.modifieds
        }
