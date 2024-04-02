import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # This is the home route
def index():             # This is the view tied to the home route
    return render_template("index.html") # This will render the index.html template


@app.route("/inspiration") # This is the about route
def inspiration():  #This is a view 
    return render_template("inspiration.html", page_title="Inspiration") # This will render the about.html template


@app.route("/contact") # This is the about route
def contact():  #This is a view 
    return render_template("contact.html", page_title="Contact") # This will render the about.html template


@app.route("/careers") # This is the about route
def careers():  #This is a view 
    return render_template("careers.html", page_title="Careers") # This will render the about.html template


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "localhost"), # This allows the app to run on any IP address
        port=int(os.getenv("PORT", 5000)), #5000 is the default port for Flask
        debug=True # This will allow for debugging messages in the console
    )
