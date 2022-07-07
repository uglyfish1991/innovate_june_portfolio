from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)
#using the route() method on our app. This builds endpoints - i.e. it tells our app how to run depending on the browser. For example, if my user visits www.domain.com/ - the index() function will run
@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/page1')
def page1():
    return render_template("page1.html")

@my_view.route('/page2')
def page2():
    return render_template("page2.html")

@my_view.route('/page3')
def page3():
    return render_template("page3.html")

@my_view.route('/page4')
def page4():
    return render_template("page4.html")

@my_view.route('/page5')
def page5():
    return render_template("page5.html")

@my_view.route('/admin')
def admin():
    return render_template("admin.html")

#if the user types in any of these paths, redirect them to the home function instead
@my_view.route('/js')
@my_view.route('/javascript')
@my_view.route('/home')
def about_redirect():
    return redirect(url_for("my_view.index"))