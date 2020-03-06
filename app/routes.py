import os,time
from app import app, model
from flask import render_template, flash, redirect, url_for, request, jsonify
import random # get this out of this


app.url_map.strict_slashes = False

@app.route('/')
@app.route('/index')
def index():
    entries = model.load_live_news()
    return render_template(
        'live.html.j2',
        entries = entries
        )

@app.route('/explore/')
@app.route('/explore/<source>')
def explore(source=None):
    if source == None:
        yaml_keys = model.get_news()
        random_news = yaml_keys[random.randint(0,len(yaml_keys)-1)]
        entries = model.explore(random_news)
    else:
        entries = model.explore(source)

    return render_template(
        'csv_list.html.j2',
        entries = entries
        )


@app.route('/live')
def live():
    entries = model.load_live_news()
    return render_template(
        'live.html.j2',
        entries = entries
        )

### API starts here ###

@app.route('/api/cache')
@app.route('/api/cache/<source>')
def cache(source=None):
    if source == None:
        cache_resp = model.get_news()
    else: #add an elsif if key not found in     yaml_keys = list(out['news'].keys())
        cache = model.make_cache(source)
        cache_resp = f'cache made for {source}'
    return jsonify(cache_resp)

@app.route('/api/generate_cache')
def generate_cache():
    msg = model.populate_news()
    return jsonify(msg)


@app.route('/api/get_cache_info')
def get_cache_info():
    directory = 'data/'
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime)]) #[file,most_recent_access,created]
    return jsonify(file_list)
