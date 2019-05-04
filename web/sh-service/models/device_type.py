"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from . import db, TableName


class DeviceType(db.Model):
    __tablename__ = TableName.DEVICE_TYPE

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    #device = db.relationship('Device', backref=TableName.DEVICE, lazy=True)
    #device_configuration = db.relationship('DeviceConfiguration', backref=TableName.DEVICE_CONFIGURATION, lazy=True)

    def __int__(self):
        pass

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return 'id: {}, name: {}, description: {}'.format(self.id, self.name, self.description)

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
        return DeviceType.query.all()

    @staticmethod
    def get_by_id(id):
        return DeviceType.query.get(id)

    @staticmethod
    def get_by_name(name):
        return DeviceType.query.filter_by(name=name).first()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
