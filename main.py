from config import app, Flask, render_template
from random import randint
from models import Flat


@app.route("/")
def index():
    return render_template("flats.html")


@app.route("/cats/")
def cats():
    cat_name = "Barsic"
    return render_template("cats.html", cat_name=cat_name)


@app.route("/f/")
def f_view():
    f = Flat.query.all()
    return render_template("index.html", f=f)


@app.route("/flats/")
def flats_view():
    flats = Flat.query.all()
    return render_template("flats.html", flats=flats)


@app.route("/flat/<flat_id>")
def flat_view(flat_id):
    flat = Flat.query.get(int(flat_id))
    return render_template("flats.html", flat=flat)


@app.route("/info/<name>/<age>")
def info(name, age):
    text = f"<h2><i>Hi {name}, you are {age} y.o.</i></h2>"
    return text


@app.route("/random/<a>/<b>")
def random(a, b):
    r = randint(int(a), int(b))
    return str(r)


app.run(debug=True)
