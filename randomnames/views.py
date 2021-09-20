from flask import Flask, render_template, jsonify, request
from .names import get_full_name

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route('/')
def index():
    args = request.args
    lower = ''
    separator = ' '
    number = ''
    if 'separator' in args:
        separator = args['separator']
    if 'lower' in args:
        lower = bool(args['lower'])
    if 'number' in args:
        number = int(args['number'])
    randomname = get_full_name(lower, separator, number)
    return render_template('index.html', randomname=randomname)

@app.route('/api/randomnames')
def api():
    args = request.args
    lower = ''
    separator = ' '
    number = ''
    if 'separator' in args:
        separator = args['separator']
    if 'lower' in args:
        lower = bool(args['lower'])
    if 'number' in args:
        number = int(args['number'])
    randomname = get_full_name(lower, separator, number)
    return jsonify(randomname)

if __name__ == "__main__":
    app.run()
