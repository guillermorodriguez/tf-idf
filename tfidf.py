import argparse
import os
from graph import *
from statistics import *

print('Started ....')

parser = argparse.ArgumentParser(prog='tfidf.py')
parser.add_argument('-graph', help='Graphical Data Output [NO | YES]')
parser.add_argument('-statistics', help='Statistical Data Output [NO | YES]')
parser.add_argument('-query', help='Query String')
parse = parser.parse_args()

if parse.graph and parse.statistics:

    _path = os.getcwd() + '\\Data\\'
    _type = '.txt'
    _skip_first = True
    _content = {}

    # Read Data set
    for _file in os.listdir(_path):
        if _type in _file:
            with open(_path + _file) as _from:
                for _line in _from:
                    # Company Description Detail in Second Column of Data Input
                    _content[_file.replace(_type, '')] += (_line.split('\t')[1]) + ' '


    print(_content)

    # Get Statistics
    _statistics = statistics()

    # Create Graphical Elements

else:
    parser.print_help()

print('Completed ....')