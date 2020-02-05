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
        # entryAll[i].content= entryAll[i].content.a.decompose()
        i += 1

    entriesProcessed = entryAll
        # for i in range(length):
    #     print(entryAll[i]    )
    # for k, v in entryAll.items():
    #     print(k , " :: ", v )

    # dict_keys(['title', 'title_detail', 'summary', 'summary_detail', 'links', 'link', 'id', 'guidislink', 'published', 'published_parsed'])
    eshort = BeautifulSoup(entry.summary, features="html.parser")
    eshort.img.decompose()
    eshort.a.decompose()
    # shorted = eshort[0:55]



    return render_template(
        'index.html.j2',
        esummary = entry.summary,
        edescription = eshort ,
        entryAll = entryAll ,
        etitle = entry.title ,
        edate = entry.published ,
        etest = entry.summary ,
        eimage = eimage,
        elink = entry.link,

        )
