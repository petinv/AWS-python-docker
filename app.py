from flask import Flask, render_template, request
from urllib.parse import unquote as url_unquote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def greet():
    name = request.form['name']
    greeting = f'Привет, {name}!'
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

