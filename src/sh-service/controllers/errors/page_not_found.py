"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, render_template

page_not_found = Blueprint(__name__, __name__, template_folder='templates')


@page_not_found.errorhandler(404)
def page_not_found_view(error):
    return "none"