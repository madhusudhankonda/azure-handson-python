from flask import Flask
app = Flask(__name__)

# Default rout
@app.route("/")
def home():
    return "<h1>Hello, Azure World!!</h1>"