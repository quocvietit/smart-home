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


class Device(db.Model):
    __tablename__ = TableName.DEVICE

    id = db.Column(db.Integer, primary_key=True)
    mqtt_topic = db.Column(db.String(255), nullable=False)
    socket_topic = db.Column(db.String(255), nullable=False)
    last_activity = db.Column(db.DateTime, nullable=False)
    is_connect = db.Column(db.Boolean, nullable=False, default=False)
    is_enable = db.Column(db.Boolean, nullable=False, default=False)
    is_control = db.Column(db.Boolean, nullable=False, default=False)

    type_id = db.Column(db.Integer, db.ForeignKey('device_type.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('device_location.id'), nullable=False)

   # device_status = db.relationship('DeviceStatus', backref=TableName.DEVICE_STATUS, lazy=True)

    def __init__(self):
        pass

    def __init__(self, type_id, location_id, mqtt_topic, socket_topic="", is_connect=False, is_enable=False, is_control=False):
        self.type_id = type_id
        self.location_id = location_id
        self.mqtt_topic = mqtt_topic
        self.socket_topic = socket_topic
        self.last_activity = datetime.now()
        self.is_connect = is_connect
        self.is_enable = is_enable
        self.is_control = is_control

    def __repr__(self):
        return 'id: {}, type_id: {}, location_id: {}, mqtt_topic: {}, socket_topic: {},' \
               'last_activity: {}, is_connect: {}, is_enable: {}, is_control: {}'.format(self.id, self.type_id,
                                                                                         self.location_id,
                                                                                         self.mqtt_topic,
                                                                                         self.socket_topic,
                                                                                         self.last_activity,
                                                                                         self.is_connect,
                                                                                         self.is_enable,
                                                                                         self.is_control)

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
        return Device.query.all()

    @staticmethod
    def get_by_id(id):
        return Device.query.get(id)

    @staticmethod
    def get_by_type_id_and_location_id(type_id, location_id):
        return Device.query.filter_by(type_id=type_id, location_id=location_id).first()

    def serialize(self):
        return {
            'id': self.id,
            'type_id': self.type_id,
            'location_id': self.location_id,
            'mqt_topic': self.mqtt_topic,
            'socket_topic': self.socket_topic,
            'last_activity': self.last_activity,
            'is_connect': self.is_connect,
            'is_enable': self.is_enable,
            'is_control': self.is_control
        }
