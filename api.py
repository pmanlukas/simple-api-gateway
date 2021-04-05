from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'
  
@app.route('/zen', methods=['GET'])
def get_zen():
    zen = requests.get("https://api.github.com/zen").text
    return zen

if __name__ == '__main__':
    app.run()
