from os.path import abspath, join, dirname
import random
import argparse
import sys

# static files for list of adj and names
adj_file = 'dico.adj.lst'
adj_path = abspath(join(dirname(__file__), adj_file))
name_file = 'dico.name.lst'
name_path = abspath(join(dirname(__file__), name_file))

# function to get a random name in a file
def get_name(filename, size):
    # open the file strip the line and loop to 
    with open(filename, 'r') as f:
        names = [line.strip() for line in f]
        if size:
            names = [name for name in names if len(name) == size]
    try:
        random_name = random.choice(names)
        return random_name
    except IndexError as idx_error:
        sys.exit(f'[ERR: {idx_error}] - No name with {size} characters, please try to increase the number of character')

def get_full_name(lower=False, separator=' ', size=''):
    full_name = f'{get_name(adj_path, size)}{separator}{get_name(name_path, size)}'
    if lower:
        return full_name.lower()
    else:
        return full_name

def main():
    parser = argparse.ArgumentParser(description='Cool random name generator')
    parser.add_argument('-l', '--lower', action='store_true', help='lower name')
    parser.add_argument('-s', '--separator', default=' ', help='specify the separator')
    parser.add_argument('-ns', '--noseparator', action='store_true', help='no separator')
    parser.add_argument('-n', '--number', type=int, help='number of letters by name')
    args = parser.parse_args()
    separator = '' if args.noseparator else args.separator
    print(get_full_name(args.lower, separator, args.number))

if __name__ == "__main__":
    main()