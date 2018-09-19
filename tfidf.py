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

if parse.graph and parse.statistics and parse.query:

    _path = os.getcwd() + '\\Data\\'
    _type = '.txt'
    _skip_first = True
    _content = {}
    _token = {}
    _lem = {}
    _stem = {}
    _tf = {}
    _idf = {}
    _tfidf = {}

    # Read Data set=
    for _file in os.listdir(_path):
        if _type in _file:
            with open(_path + _file) as _from:
                for _line in _from:
                    # Company Description Detail in Second Column of Data Input
                    if _file.replace(_type, '') in _content:
                        _content[_file.replace(_type, '')] += ' ' + (_line.split('\t')[1])
                    else:
                        _content[_file.replace(_type, '')] = (_line.split('\t')[1])

    # Get Statistics
    _statistics = statistics()
    for _doc in _content.keys():
        if len(_content[_doc].strip()) > 0:
            _token[_doc] = _statistics.tokenization(_content[_doc])
            _lem[_doc] = _statistics.lemmatization(_content[_doc])
            _stem[_doc] = _statistics.stemminization(_content[_doc])

            for element in parse.query.split(' '):
                _tf[_doc + '-' + element] = _statistics.tf(_stem[_doc], element)

    for element in parse.query.split(' '):
        _idf[element] = _statistics.idf(_content, element, _stem)

    print("Tokens:")
    print(_token)

    print("Lemmatization:")
    print(_lem)

    print("Stemming:")
    print(_stem)

    print("Term Frequency:")
    print(_tf)

    print("Inverse Document Frequency")
    print(_idf)

    print("Term Frequency - Inverse Document Frequency")
    print(_tfidf)

    # Create Graphical Elements
    _graph = graph()

else:
    parser.print_help()

print('Completed ....')