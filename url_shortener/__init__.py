from flask import Flask
from .extensions import db
from .routes import short
from .models import Link

from apscheduler.schedulers.background import BackgroundScheduler


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(short)

    return app

# link = Link()
# scheduler = BackgroundScheduler(daemon=True)
# scheduler.add_job(link.cleanup(), "interval", minutes=1)
# scheduler.start()
