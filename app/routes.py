from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    posts = [
      {
          'author': {'username': 'John'},
          'body': 'Beautiful day in Belgrade!'
      },
      {
          'author': {'username': 'Susan'},
          'body': 'The Avengers movie was so cool!'
      }
    ]
    return render_template('index.html.j2', title='DSS Reader', posts=posts)
