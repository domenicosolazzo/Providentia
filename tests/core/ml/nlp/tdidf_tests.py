from nose.tools import *
from providentia.core.ml.nlp.tdidf import TdIdf

def test_frequency_of_a_word():
    document = "abc abc abc ciao I am Domenico"
    word = "abc"
    tdidf = TdIdf(word, document, [])
    result = tdidf.frequency(document)
    assert_equal(3, result)

def test_word_count():
    document = "I am Domenico"
    tdidf = TdIdf("", document, [])
    result = tdidf.wordcount()
    assert_equal(13, result)

def test_num_docs_containing_word():
    documentList = ["I am Domenico", "Let's watch tv", "Domenico watches tv"]
    tdidf = TdIdf("Domenico", "", documentList)
    result = tdidf.numDocsContainingWord()
    assert_equal(2, result)