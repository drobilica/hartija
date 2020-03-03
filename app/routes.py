from app import app, model
from app.model import load_sample_csv
from flask import render_template, flash, redirect, url_for, request, jsonify


def return_cache(tmp_file,update_time_sec):
    return None


@app.route('/')
@app.route('/index')
def index():
    entries = model.load_sample_csv()

    return render_template(
        'fixedlist.html.j2',
        entries = entries
        )


@app.route('/live')
def live():
    entries = model.load_live_news()
    return render_template(
        'live.html.j2',
        entries = entries
        )

@app.route('/api/make-cache')
def cache():
    cache = model.make_cache()
    cache_resp = "cache made "
    return jsonify(cache_resp)