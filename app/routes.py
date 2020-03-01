from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime
import pandas as pd
import feedparser
from bs4 import BeautifulSoup

def return_cache(tmp_file,update_time_sec):
    return None

@app.route('/')
@app.route('/index')
def index():

    NewsFeed = feedparser.parse("https://www.eurogamer.net/?format=rss&type=article")
    # NewsFeed = feedparser.parse("https://distrowatch.com/news/dw.xml")
    # NewsFeed = feedparser.parse("http://www.politika.rs/rss/")
    # NewsFeed = feedparser.parse("https://www.gamasutra.com/blogs/rss/")
    # NewsFeed = feedparser.parse("https://isthereanydeal.com/rss/specials/eu2/")
    # NewsFeed = feedparser.parse("https://www.psxhax.com/articles/index.rss")

    rawrss = [
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
        # 'https://www.yahoo.com/news/rss/',
        'http://www.huffingtonpost.co.uk/feeds/index.xml',
        'http://feeds.feedburner.com/TechCrunch/',
        ]

    feeds = [] # list of feed objects

    for url in rawrss:
        feeds.append(feedparser.parse(url))

    posts = [] # list of posts [(title1, link1, summary1), (title2, link2, summary2) ... ]


    for feed in feeds:
        for post in feed.entries:
            # print(post.link)
            posts.append((post.title, post.link, post.summary))

    df = pd.DataFrame(posts, columns=['title', 'link', 'summary']) # pass data to init

    print(df.info())
    NewsFeed = feedparser.parse("https://www.eurogamer.net/?format=rss&type=article")


    entryAll = NewsFeed.entries

    i=0
    while i < len(entryAll):
        soupy = BeautifulSoup(entryAll[i].summary, features="html.parser")
        entryAll[i].img = soupy.img
        entryAll[i].content = soupy.p
        i += 1

    return render_template(
        'index.html.j2',
        entryAll = entryAll ,
        )
