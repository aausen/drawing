"""Server for drawing application."""

from flask import Flask
from flask.templating import render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = ['secret_key']
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def show_index():
    """"Displays index page."""

    return render_template("index.html")

if __name__=="__main__":

    app.run(host="0.0.0.0", debug=True)