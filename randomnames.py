from flask import Flask, render_template
from os.path import abspath, join, dirname
import random

app = Flask(__name__)

adj_file = 'dico.adj.lst'
adj_path = abspath(join(dirname(__file__), adj_file))

name_file = 'dico.name.lst'
name_path = abspath(join(dirname(__file__), name_file))

def get_name(filename):
    with open(filename, 'r') as f:
        name = [line.strip() for line in f]
        return random.choice(name)

def get_full_name():
    return "{0} {1}".format(get_name(adj_path), get_name(name_path))

@app.route('/')
def index():
    coolname = get_full_name()
    return render_template('index.html', coolname=coolname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
