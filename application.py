from flask import Flask
app = Flask(__name__)

# Default route
@app.route("/")
def home():
    return "<h1>Hello, Azure World! How are you all?</h1>"