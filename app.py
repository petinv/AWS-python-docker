# for testing Actions Github 1.0

from flask import Flask, render_template, request

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
    app.run(debug=True)
