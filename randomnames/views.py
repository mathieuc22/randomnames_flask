from flask import Flask, render_template, jsonify
from .names import get_full_name

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route('/')
def index():
    randomname = get_full_name()
    return render_template('index.html', randomname=randomname)

@app.route('/api/randomnames')
def refresh():
    return jsonify(get_full_name())

if __name__ == "__main__":
    app.run()
