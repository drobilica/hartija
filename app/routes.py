from app import app, model
from app.model import load_sample_csv
from flask import render_template, flash, redirect, url_for, request



def return_cache(tmp_file,update_time_sec):
    return None

@app.route('/')
@app.route('/index')
def index():
    entries = model.load_sample_csv()

    return render_template(
        'index.html.j2',
        entries = entries
        )
