from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for

import sqlite3   #enable control of an sqlite database
import datetime

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for("home"))

if __name__=='__main__':
    app.debug = True
    app.run()
