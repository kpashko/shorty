from flask import Blueprint, render_template, request, redirect
from .models import Link
from datetime import datetime, timedelta

from .extensions import db

short = Blueprint('short', __name__)


@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    if link.original_url[:4] not in ("http", "ftp:"):
        return redirect('https://'+link.original_url)
    return redirect(link.original_url)


@short.route('/')
def index():
    return render_template("index.html")


@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    lifetime = int(request.form.get('lifetime'))
    expiry = datetime.now()+timedelta(days=lifetime)
    link = Link(original_url=original_url, expiration_date=expiry)

    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html',
                           new_link=link.short_url, original_url=link.original_url)


@short.errorhandler(404)
def page_not_found(e):
    return '404', 404

###########
#          #
#   API's  ###
#          ####
##################


@short.route('/api/get_info/<short_url>')
def api_get_url_info(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    res = {"original url" : link.original_url, "creation date:" : link.date_created.strftime("%B %d, %Y"),
           "expiration date:" : link.expiration_date.strftime("%B %d, %Y")}
    return render_template('response.html', res=res)


@short.route('/api/s/<path:original_url>')
def api_shorten_url(original_url):
    link = Link(original_url=original_url)

    db.session.add(link)
    db.session.commit()

    return link.short_url


@short.route('/api/all')
def stats():
    links = Link.query.all()
    return render_template('all.html', links=links)



