from os.path import abspath, join, dirname
import random

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
