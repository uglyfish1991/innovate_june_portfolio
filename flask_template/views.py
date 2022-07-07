from flask import Flask, render_template, Blueprint, redirect, url_for, request
from favs import fav_bands

my_view = Blueprint('my_view', __name__)
#using the route() method on our app. This builds endpoints - i.e. it tells our app how to run depending on the browser. For example, if my user visits www.domain.com/ - the index() function will run
@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/katy')
def katy():
    return render_template("katy.html")

@my_view.route('/about', methods=["GET","POST"])
def about():
    if request.method =="POST":
        new_band=request.form["add_band"]
        fav_bands.append(new_band)
    return render_template("about.html", fav_bands = fav_bands)


#if the user types in any of these paths, redirect them to the home function instead
@my_view.route('/aboutkaty')
@my_view.route('/aboutme')
def about_redirect():
    return redirect(url_for("my_view.about"))