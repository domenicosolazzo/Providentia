import math
from operator import itemgetter
class TdIdf(object):
    word = ""
    document = ""
    document_list = []

    def __init__(self, word, document, documentList):
        self.word = word
        self.document = document
        self.document_list = documentList

    def frequency(self, word, document):
        """
        Frequency of a word in a given document
        :return: Frequency of a word in a given document
        """
        return document.count(word)

    def word_count(self, document):
        """
        Word count in a document
        :return: Number of characters in a document
        """
        return len(document)

    def num_docs_containing_word(self, word, document_list):
        """
        Number of document containing a given word
        :return: The number of documents containing a given word
        """
        count = 0
        for doc in document_list:
            if self.frequency(word, doc) > 0:
              count += 1
        return count

    def tf(self, word, document):
        """
        Term frequency of a word in given document
        :param word: A given word
        :param document: A given document
        :return: term frequency
        """
        return (self.frequency(word,document) / float(self.word_count(document)))


    def idf(self, word, documentList):
        """
        The inverse document frequency is a measure of how much information the word provides, that is,
        whether the term is common or rare across all documents. It is the logarithmically scaled fraction of the documents
        that contain the word, obtained by dividing the total number of documents
        by the number of documents containing the term, and then taking the logarithm of that quotient.
        :param word:
        :param documentList:
        :return:
        """
        return math.log(len(documentList) / self.num_docs_containing_word(word,documentList))