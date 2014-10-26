from tdidf import TfIdf
import operator
class Keywords(object):
    def __init__(self, number_of_keywords=1):
        self.number_of_keywords = number_of_keywords


    def top_keywords_in_document(self, doc, corpus):
        """
        Top n keywords for a document compared with a corpus
        :param doc: The document
        :param corpus: The corpus of documents
        :return: The top n keywords for the document
        """
        word_dictionary = {}
        for word in set(doc):
            word_dictionary[word] = TfIdf(word,doc,corpus)
        sorted_d = sorted(word_dictionary.iteritems(), key=operator.itemgetter(1))
        sorted_d.reverse()
        return [w[0] for w in sorted_d[:self.number_of_keywords]]

    def top_keywords_in_corpus(self, corpus):
        """
        Top keywords in a corpus
        :param corpus: The corpus
        :return:Top keywords in a corpus
        """
        keyword_list = set()
        [[keyword_list.add(x) for x in self.top_keywords_in_document(doc,corpus)] for doc in corpus]
        return keyword_list
