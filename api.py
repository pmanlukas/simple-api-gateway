from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
@app.route('/zen')
def get_zen():
    zen = requests.get("https://api.github.com/zen")
    return zen  

@app.route('/octocat')
def get_octocat():
    return 'Hello, World!'
