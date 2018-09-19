"""
    @ Author:       Guillermo Rodriguez
    @ Date:         09/18/2018
    @ Purpose:      Apply tokenization, lemmatization, and stemming to a data set.
                    Common point for the calculation of TF / IDF statistics.
    @ Dependency:   NLTK
                        python
                        >>> import nltk
                        >>> nltk.download()
"""

# python
# import nltk
# nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import math

class statistics:

    """
        Constructor
    """
    def __init__(self):
        print('Statistics Object Initialized')

    """
        @ Author:       Guillermo Rodriguez
        @ Date:         09/18/2018
        @ Purpose:      Lemmatization a data set
    """
    def lemmatization(self, data):
        result = {}

        lemmatizer = WordNetLemmatizer()

        for _token in data.split(' '):
            _word = lemmatizer.lemmatize(_token)

            if _word in result:
                result[_word] += 1
            else:
                result[_word] = 1

        return result

    """
        @ Author:       Guillermo Rodriguez
        @ Date:         09/18/2018
        @ Purpose:      Steminization a data set
    """
    def stemminization(self, data):
        result = {}

        stemmer = PorterStemmer()

        for _token in data.split(' '):
            _word = stemmer.stem(_token)

            if _word in result:
                result[_word] += 1
            else:
                result[_word] = 1

        return result

    """
        @ Author:       Guillermo Rodriguez
        @ Date:         09/18/2018
        @ Purpose:      Tokenize a data set
    """
    def tokenization(self, data):
        result = {}

        for _word in data.split(' '):
            _word = _word.strip()

            if _word in result:
                result[_word] += 1
            else:
                result[_word] = 1

        return result

    """
        @ Author:       Guillermo Rodriguez
        @ Date:         09/18/2018
        @ Purpose:      Calculate term frequency (tf)
    """
    def tf(self, entries, word):
        total = 0
        length = 0
        _root_word = PorterStemmer().stem(WordNetLemmatizer().lemmatize(word))

        for entry in entries:
            length += len(entry)
            if entry == _root_word:
                total += 1

        if length > 0:
            return total / length

        return 0

    """
        @ Author:       Guillermo Rodriguez
        @ Date:         09/18/2018
        @ Purpose:      Calculate inverse document frequency (idf)
    """
    def idf(self, documents, word, stem):

        _root_word = PorterStemmer().stem(WordNetLemmatizer().lemmatize(word))
        _length = 0
        _found_in = 0

        for document in documents.values():
            _length += len(document.replace(' ', ''))

        for entry in stem.values():
            if _root_word in entry:
                _found_in += 1

        if _found_in == 0:
            _found_in = 1

        return math.log(_length/_found_in)