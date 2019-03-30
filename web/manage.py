"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app, db


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
