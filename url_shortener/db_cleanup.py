from datetime import datetime

from flask_apscheduler import APScheduler

from .extensions import db
from .models import Link

scheduler = APScheduler()


def cleanup():
    app = scheduler.app
    with app.app_context():
        try:
            Link.query.filter(Link.date_created <= datetime.now()).delete()
        except Exception as e:
            print(str(e))
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    return str('ok')


# if __name__ == "__main__":
#     cleanup()
