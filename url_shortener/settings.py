import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = os.environ.get('ADMIN_PASSWORD')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

# Flask-apscheduler
JOBS = [
    {
        'id': 'db_cleanup',
        'func': 'url_shortener.db_cleanup:cleanup',
        'trigger': 'cron',
        'minutes': 0,
        'hours': 0,  # triggers everyday at 00:00
        'replace_existing': True
    }
]
SCHEDULER_JOBSTORES = {
    'default': SQLAlchemyJobStore(url='sqlite:///flask_context.db')
}
SCHEDULER_API_ENABLED = True