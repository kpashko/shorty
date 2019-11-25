from datetime import datetime, timedelta
from .extensions import db
import string
from random import choices


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(4), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    expiration_date = db.Column(db.DateTime, default=datetime.now() + timedelta(days=90))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_shortlink()

    def generate_shortlink(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=4))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_shortlink()

        return short_url

    def cleanup(self):
        return self.query.filter_by(date_created=datetime.now()).delete()

