from flask import Flask
app = Flask(__name__)

# Default route
@app.route("/")
def home():
    return "<h1>Hello OLT Gurus</h1>"