from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for

import sqlite3   #enable control of an sqlite database
import datetime

import urllib.request
import urllib.error
import json
import time
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for("home"))

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/cs", methods=['GET', 'POST'])
def cs():
    return render_template('cs.html')

@app.route("/chorus", methods=['GET', 'POST'])
def chorus():
    return render_template('chorus.html')

@app.route("/essay", methods=['GET', 'POST'])
def essay():
    return render_template('essay.html')


if __name__=='__main__':
    app.debug = True
    app.run()
