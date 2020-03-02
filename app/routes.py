from app import app, model
from app.model import load_sample_csv
from flask import render_template, flash, redirect, url_for, request



def return_cache(tmp_file,update_time_sec):
    return None


@app.route('/')
@app.route('/index')
def index():
    entries = model.load_sample_csv()

    # print(entries['0'])
    # print(entries["title"])
    # print(entries.keys())
    # keys = list(entries.keys())
    # values = list(entries.values())
    # print(keys)
    # print(values)


    return render_template(
        'index.html.j2',
        entries = entries
        )

@app.route('/live')
def live():
    entries = model.load_live_news()
    return render_template(
        'testiterate.html.j2',
        entries = entries
        )

@app.route('/csv')
def csv():
    entries = model.generate_csv()
    return render_template(
        'testiterate.html.j2',
        entries = entries
        )
