class TdIdf(object):
    word = ""
    document = ""
    document_list = []

    def __init__(self, word, document, documentList):
        self.word = word
        self.document = document
        self.document_list = documentList

    def frequency(self, document):
        """
        Frequency of a word in a given document
        :return: Frequency of a word in a given document
        """
        return document.count(self.word)

    def wordcount(self):
        """
        Word count in a document
        :return: Number of characters in a document
        """
        return len(self.document)

    def numDocsContainingWord(self):
        """
        Number of document containing a given word
        :return: The number of documents containing a given word
        """
        count = 0
        for document in self.document_list:
            if self.frequency(document) > 0:
              count += 1
            return count