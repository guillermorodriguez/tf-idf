"""
    @ Author:       Guillermo Rodriguez
    @ Date:         09/18/2018
    @ Purpose:      Apply tokenization, lemmatization, and stemming to a data set
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

class statistics:

    """
        Constructor
    """
    def __init__(self):
        print('Statistics Object Initialized')

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
        @ Purpose:      Tokenize a data set
    """
    def lemmatization(self, tokenized_data):
        result = {}

        lemmatizer = WordNetLemmatizer()

        for _token in tokenized_data:
            _word = lemmatizer.lemmatize(_token)

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
    def stemminization(self, tokenized_data):
        result = {}

        stemmer = PorterStemmer()

        for _token in tokenized_data:
            _word = stemmer.stem(_token)

            if _word in result:
                result[_word] += 1
            else:
                result[_word] = 1

        return result
