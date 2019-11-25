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

    scheduler.init_app(app)
    scheduler.start()

    return app


# import from other_module...
# To avoid SQLAlchemy circular import, do the import at the bottom.
from .db_cleanup import scheduler

# link = Link()
# scheduler = BackgroundScheduler(daemon=True)
# scheduler.add_job(link.cleanup(), "interval", minutes=1)
# scheduler.start()
