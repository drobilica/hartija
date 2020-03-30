import pandas as pd
import feedparser
import csv
from bs4 import BeautifulSoup
from collections import defaultdict
import yaml
import threading

def explore(source):
    df = pd.read_csv(f"data/{source}_data.csv")
    return df


def load_live_news():
    NewsFeed = feedparser.parse("https://www.eurogamer.net/?format=rss&type=article")
    entries = NewsFeed.entries
    i=0
    while i < len(entries):
        soupy = BeautifulSoup(entries[i].summary, features="html.parser")
        entries[i].img = soupy.img
        entries[i].content = soupy.p
        i += 1
    return entries




def make_cache(source):
    with open("conf/rss-feeds.yaml", 'r') as stream:
        out = yaml.load(stream, Loader=yaml.Loader)

    def list_append(url, feeds):
        feeds.append(feedparser.parse(url))
    jobs = []

    for url in out['news'][source]:
        feeds = []
        thread = threading.Thread(target=list_append(url, feeds))
        jobs.append(thread)
        print(url)

    for j in jobs:
        j.start()


    for j in jobs:
        j.join()
    
    posts = [] # list of posts [(title1, link1, summary1), (title2, link2, summary2) ... ]

    for feed in feeds:
        for post in feed.entries:
            # print(post.link)
            posts.append((post.title, post.link, post.summary))

    df = pd.DataFrame(posts, columns=['title', 'link', 'summary']) # pass data to init
    df.to_csv(f'data/{source}_data.csv')


def get_news():
    with open("conf/rss-feeds.yaml", 'r') as stream:
        out = yaml.load(stream, Loader=yaml.Loader)
    yaml_keys = list(out['news'].keys()) # a list

    return yaml_keys


def populate_news():
    for i in get_news():
        make_cache(i)
    return "Cache made for all news"
