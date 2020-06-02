from flask import Flask, render_template
from .names import get_full_name

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route('/')
def index():
    randomname = get_full_name()
    return render_template('index.html', randomname=randomname)

@app.route('/refresh')
def refresh():
    randomname = get_full_name()
    return randomname

if __name__ == "__main__":
    app.run()
