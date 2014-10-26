class TdIdf(object):
    word = ""
    document = ""
    document_list = []

    def __init__(self, word, document, documentList):
        self.word = word
        self.document = document
        self.document_list = documentList

    def frequency(self):
        """
        Frequency of a word in a given document
        :return: Frequency of a word in a given document
        """
        return self.document.count(self.word)

    def wordcount(self):
        """
        Word count in a document
        :return: Number of characters in a document
        """
        return len(self.document)
    