from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime

import feedparser
from bs4 import BeautifulSoup

def return_cache(tmp_file,update_time_sec):
    return None

@app.route('/')
@app.route('/index')
def index():

    NewsFeed = feedparser.parse("https://www.eurogamer.net/?format=rss&type=article")

    entry = NewsFeed.entries[0]

    entryAll = NewsFeed.entries
    print(type(entryAll))
    print(type(entryAll[9]))

    soup = BeautifulSoup(entry.summary, features="html.parser")
    eimage = soup.img
    i=0

    while i < len(entryAll):
        soupy = BeautifulSoup(entryAll[i].summary, features="html.parser")
        entryAll[i].img = soupy.img
        entryAll[i].content= soupy.p
        i += 1

    return render_template(
        'index.html.j2',
        esummary = entry.summary,
        entryAll = entryAll ,
        etitle = entry.title ,
        etest = entry.summary ,
        eimage = eimage,
        elink = entry.link,

        )
