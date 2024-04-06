import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")  # This is the home route
def index():             # This is the view tied to the home route
    return render_template("index.html") # This will render the index.html template


@app.route("/inspiration") # This is the about route
def inspiration():  #This is a view 
    data = []
    with open("data/inspiration.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("inspiration.html", page_title="Inspiration", inspiration=data ) # This will render the inspiration.html template


@app.route("/contact", methods=["GET", "POST"]) # This is the about route
def contact():  #This is a view 
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact") # This will render the about.html template


@app.route("/careers") # This is the about route
def careers():  #This is a view 
    return render_template("careers.html", page_title="Careers") # This will render the about.html template


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",  # Listen on all available network interfaces
        port=int(os.getenv("PORT", 5000)),  # Use the PORT environment variable provided by Heroku, default to 5000 if not set
        debug=False
    )
