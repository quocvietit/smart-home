"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
from flask import Blueprint, render_template, jsonify
from models.type_model import TypeModel

home = Blueprint(__name__, __name__, template_folder='templates')


@home.route('/')
@home.route('/index')
@home.route('/home')
def home_view():
    return render_template('home/index.html')


@home.route('/tem')
def test():
    logging.info("get Date")
    data = TypeModel.get(1)
    print (data.name)
    if data:
        return jsonify(data.serialize())
    return  (jsonify([data.serialize() for data in TypeModel.query.all()]))
