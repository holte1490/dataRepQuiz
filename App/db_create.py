import sys
import os

sys.path.append(os.getcwd()[:os.getcwd().index('BCS')])

from migrate.versioning import api
from BCS.App.config import SQLALCHEMY_DATABASE_URI
from BCS.App.config import SQLALCHEMY_MIGRATE_REPO
from BCS.App.app import db
import os.path

db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))