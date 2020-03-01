import pandas as pd
import feedparser
import csv
from bs4 import BeautifulSoup


def load_sample_csv():
    columns = []
    with open(file,'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if columns:
                for i, value in enumerate(row):
                    columns[i].append(value)
            else:
                # first row
                columns = [[value] for value in row]
    # you now have a column-major 2D array of your file.
    as_dict = {c[0] : c[1:] for c in columns}
    print(as_dict)

    file = csv.reader(open('sample_data.csv'), delimiter=',')
    for line in file:
        print(line)


NewsFeed = feedparser.parse("https://www.eurogamer.net/?format=rss&type=article")
# NewsFeed = feedparser.parse("https://distrowatch.com/news/dw.xml")
# NewsFeed = feedparser.parse("http://www.politika.rs/rss/")
# NewsFeed = feedparser.parse("https://www.gamasutra.com/blogs/rss/")
# NewsFeed = feedparser.parse("https://isthereanydeal.com/rss/specials/eu2/")
# NewsFeed = feedparser.parse("https://www.psxhax.com/articles/index.rss")

rawrss = [
    'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
    # 'https://www.yahoo.com/news/rss/',
    # 'http://www.huffingtonpost.co.uk/feeds/index.xml',
    'http://feeds.feedburner.com/TechCrunch/',
    ]

feeds = [] # list of feed objects

for url in rawrss:
    feeds.append(feedparser.parse(url)) # type list

posts = [] # list of posts [(title1, link1, summary1), (title2, link2, summary2) ... ]


for feed in feeds:
    for post in feed.entries:
        # print(post.link)
        posts.append((post.title, post.link, post.summary))

df = pd.DataFrame(posts, columns=['title', 'link', 'summary']) # pass data to init
df.to_csv(r'/home/mrle/dev/hartija/sample_data.csv')
# print(df.info())
# print(df.title)

entryAll = NewsFeed.entries
#    entryAll = feeds.entries
# df.to_string()
i=0
while i < len(entryAll):
    soupy = BeautifulSoup(entryAll[i].summary, features="html.parser")
    entryAll[i].img = soupy.img
    entryAll[i].content = soupy.p
    i += 1
