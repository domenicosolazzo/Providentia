from nltk import wordpunct_tokenize
from bs4 import BeautifulSoup
from providentia.core.ml.nlp.tdidf import TfIdf

class DocumentHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def words_longer_than(words_list, length):
        if not isinstance(words_list, list):
            raise Exception("The words_list must be a list")
        return [word.lower() for word in words_list if len(word) > length]

    @staticmethod
    def wordpunct_tokenize(document):
        """
        Convert the text in tokens
        :param document: The document text
        :return: A list of tokens
        """
        return wordpunct_tokenize(document)

    @staticmethod
    def remove_html_markup(html_document):
        """
        Clean up the html markup from a document
        :param html_document: The html document
        :return: The text from the html document
        """
        html_parser = BeautifulSoup(html_document)
        return html_parser.get_text()

    @staticmethod
    def create_feature_vector(self, corpus, top_keywords):
        """
        Now that we have this superset of keywords, we need to go through each document again and
        compute TF-IDF for each term. Thus, this will be likely be a sparse vector as most of the entries will be zero.
        """
        feature_vectors=[]
        n=len(corpus)

        for document in corpus:
            vec=[]
            [vec.append(TfIdf(word, document, corpus).calculate() if word in document else 0) for word in top_keywords]
            feature_vectors.append(vec)




