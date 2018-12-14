from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celeryapp import app as celery_app
import pymysql

__all__ = ('celery_app',)

pymysql.install_as_MySQLdb()