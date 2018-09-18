import argparse

print('Started ....')

parser = argparse.ArgumentParser(prog='tfidf.py')
parser.add_argument('-graph', help='Graphical Data Output [NO | YES]')
parser.add_argument('-statistics', help='Statistical Data Output [NO | YES]')
parse = parser.parse_args()

if parse.graph and parse.statistics:


else:
    parser.print_help()

print('Completed ....')