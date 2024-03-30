import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # This is the home route
def index():             # This is the view tied to the home route
    return render_template("index.html") # This will render the index.html template

@app.route("/about") # This is the about route
def about():  #This is a view 
    return render_template("about.html") # This will render the about.html template

@app.route("/contact") # This is the about route
def contact():  #This is a view 
    return render_template("contact.html") # This will render the about.html template

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "localhost"), # This allows the app to run on any IP address
        port=int(os.getenv("PORT", 5000)), #5000 is the default port for Flask
        debug=True # This will allow for debugging messages in the console
    )
