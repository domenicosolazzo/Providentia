import os
from providentia.core.sources.rss.fetchers import Fetcher
from providentia.core.ml.nlp.utilities.document_utilities import DocumentHelper
from providentia.core.ml.nlp.keywords import Keywords
from providentia.core.ml.similarities.cosine import cosine_distance
from providentia.core.ml.clustering.hierarchical import HierarichicalCluster
from providentia.configurations.config import ConfigurationManager

class ProvidentiaBrain(object):
    def __init__(self):
        self.fetcher = Fetcher()
        self.config_manger = ConfigurationManager()

    def fetch_top_keywords(self):
        corpus = []
        titles = []
        document_list = []
        entries = self.fetcher.fetch_entries()
        keywords_fetcher = Keywords(self.config_manger.NUMBER_KEYWORDS)

        doc_id = 1
        for entry in entries:
            # Cleaning the description of each entry from the markup
            words = DocumentHelper.wordpunct_tokenize(DocumentHelper.remove_html_markup(entry.description))
            words.extend(DocumentHelper.wordpunct_tokenize(entry.title))
            # Lower all the words with more than a character
            lower_words=[x.lower() for x in words if len(x) > 1]
            # Add these words to a corpus
            corpus.append(lower_words)
            titles.append(entry.title)
            keywords_by_document = keywords_fetcher.top_keywords_in_document(lower_words, corpus)
            document_list.append({'id':doc_id, 'title': entry.title, 'keywords':keywords_by_document})
            doc_id = doc_id + 1

        # Fetch the top keywords from the corpus
        top_keywords = keywords_fetcher.top_keywords_in_corpus(corpus)

        return {'top_keywords': top_keywords, 'keywords_by_document':document_list}

    def winsdom(self):
        words = []
        corpus = []
        titles = []
        entries = self.fetcher.fetch_entries()
        for entry in entries:
            # Cleaning the description of each entry from the markup
            words = DocumentHelper.wordpunct_tokenize(DocumentHelper.remove_html_markup(entry.description))
            words.extend(DocumentHelper.wordpunct_tokenize(entry.title))
            # Lower all the words with more than a character
            lower_words=[x.lower() for x in words if len(x) > 1]
            # Add these words to a corpus
            corpus.append(lower_words)
            titles.append(entry.title)

        keywords_fetcher = Keywords(self.config_manger.NUMBER_KEYWORDS)
        # Fetch the top keywords from the corpus
        top_keywords = keywords_fetcher.top_keywords_in_corpus(corpus)

        # Create a feature vector
        feature_vectors = DocumentHelper.create_feature_vector(corpus, top_keywords)

        # Calculate the cosine distance similarity for each couple of documents
        mat = cosine_distance(feature_vectors, len(corpus))

        hierarchical_cluster = HierarichicalCluster()
        clusters = hierarchical_cluster.fetch_clusters(mat, len(corpus))


        return {'keywords': list(top_keywords), 'clusters':clusters, 'titles': titles}
