"""Server for drawing application."""

from flask import Flask
from flask.templating import render_template
from jinja2 import StrictUndefined
from model import Gallery, db, connect_to_db
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def show_index():
    """"Displays index page."""

    return render_template("index.html")

if __name__=="__main__":

    app.run(host="0.0.0.0")
    connect_to_db(app, os.environ.get("DATABASE_URL"))