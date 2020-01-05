from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime

import feedparser

# @app.route('/')
# @app.route('/index')
# def index():
#     posts = [
#       {
#           'author': {'username': 'John'},
#           'body': 'Beautiful day in Belgrade!'
#       },
#       {
#           'author': {'username': 'Susan'},
#           'body': 'The Avengers movie was so cool!'
#       }
#     ]
#     return render_template('index.html.j2', title='DSS Reader', posts=posts)



def return_cache(tmp_file,update_time_sec):
    return None

@app.route('/')
def index():
    entries_sorted=None
    if entries_sorted!=None:
        return render_template(
        'index.html.j2',
        entries=entries_sorted
        )
    RSS_URLS = [
        'http://www.gameinformer.com/b/MainFeed.aspx?Tags=preview',
        'http://www.polygon.com/rss/group/news/index.xml',
        ]

    entries = []
    for url in RSS_URLS:
        entries.extend(feedparser.parse(url).entries)

    entries_sorted = sorted(
        entries,
        key=lambda e: e.published_parsed,
        reverse=True)
    f = open("output.txt", "w+")
    for i in entries_sorted:
        f.write(str(i))
    f.close()
    return render_template(
        'index.html.j2',
        entries=entries_sorted
        )
