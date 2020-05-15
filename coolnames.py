from flask import Flask, render_template
from coolnames import main
app = Flask(__name__)

@app.route('/')
def index():
    coolname = main.get_full_name()
    return render_template('index.html', coolname=coolname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
