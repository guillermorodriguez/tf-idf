import argparse
import os
from graph import *
from statistics import *

print('Started ....')

parser = argparse.ArgumentParser(prog='tfidf.py')
parser.add_argument('-graph', help='Graphical Data Output [NO | YES]')
parser.add_argument('-statistics', help='Statistical Data Output [NO | YES]')
parser.add_argument('-query', help='Query String Within Quotes Unless One Entry is Given')
parse = parser.parse_args()

if parse.graph and parse.statistics and parse.query:

    _path = os.getcwd() + '\\Data\\'
    _type = '.txt'
    _skip_first = True
    _content = {}                   # Document Content
    _token = {}                     # Tokenization of Data
    _lem = {}                       # Lemmatization of Data
    _stem = {}                      # Stemming of Data
    _tf = {}                        # Term Frequency
    _idf = {}                       # Inverse Document Frequency
    _tfidf = {}                     # Term Frequency - Inverse Document Frequency
    _vs = []                        # Vector Space

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

            term_index = 0
            _vs.append([])
            for element in parse.query.split(' '):
                _tf[_doc + '-' + element] = _statistics.tf(_stem[_doc], element)

                if _tf[_doc + '-' + element] > 0:
                    _vs[len(_vs)-1].append(1)
                else:
                    _vs[len(_vs) - 1].append(0)

                term_index += 1

    for element in parse.query.split(' '):
        _idf[element] = _statistics.idf(_content, element, _stem)

    for key in _tf.keys():
        term = key.split('-')[1]
        _tfidf[key] = _tf[key] * _idf[term]

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

    print("Vector Space")
    print(_vs)

    # Create Graphical Elements
    _graph = graph()
    _graph.create_plot(_tfidf)


else:
    parser.print_help()

print('Completed ....')