from nltk import wordpunct_tokenize
from bs4 import BeautifulSoup


class DocumentHelper(object):
    def __init__(self):
        pass

    def words_longer_than(self, words_list, length):
        if not isinstance(words_list, list):
            raise Exception("The words_list must be a list")
        return [word.lower() for word in words_list if len(word) > length]

    def wordpunct_tokenize(self, document):
        """
        Convert the text in tokens
        :param document: The document text
        :return: A list of tokens
        """
        return wordpunct_tokenize(document)

    def remove_html_markup(self, html_document):
        """
        Clean up the html markup from a document
        :param html_document: The html document
        :return: The text from the html document
        """
        html_parser = BeautifulSoup(html_document)
        return html_parser.get_text()




