import os
from flask import Flask

app = Flask(__name__)

@app.route("/")  # This is the home route
def index():             # This is the function tied to the home route
    return "Hello, World!"  # This is the response

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "localhost"), # This allows the app to run on any IP address
        port=int(os.getenv("PORT", 5000)), #5000 is the default port for Flask
        debug=True # This will allow for debugging messages in the console
    )
