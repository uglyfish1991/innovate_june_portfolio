#From the module flask, import the class Flask

from flask import Flask, render_template
from views import my_view

#creating an instance of a Flask class called app
app = Flask(__name__)
app.register_blueprint(my_view)

# an error handler - rather than going to the default 404 page, we can use a custom one!
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)
# this return render template will give us back the 404 page AND the variable e - which is the error message. We pass it through as e=e

#this if statement is the last thing on our app - it allows th initialisation of the app. Debug is set to true, and we pick a port to run on. 5000 is default, 8000 is linked to the debugger
if __name__=="__main__":
    app.run(debug=True, port=8000)