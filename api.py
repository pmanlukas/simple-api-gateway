from flask import Flask
import requests
import urllib.request

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World!'
  
@app.route('/zen')
def get_zen():
    zen = requests.get("https://api.github.com/zen").text
    return zen

@app.route('/octocat')
def get_octocat():
    with urllib.request.urlopen("https://api.github.com/octocat") as response:
        html = response.read().decode("utf8")
    return html

if __name__ == '__main__':
    app.run()
