from nose.tools import *
from providentia.core.ml.nlp.tdidf import TdIdf

def test_frequency_of_a_word():
    document = "abc abc abc ciao I am Domenico"
    word = "abc"
    tdidf = TdIdf(word, document, [])
    result = tdidf.frequency(word, document)
    assert_equal(3, result)

def test_word_count():
    document = "I am Domenico"
    tdidf = TdIdf("", document, [])
    result = tdidf.word_count(document)
    assert_equal(13, result)

def test_num_docs_containing_word():
    documentList = ["I am Domenico", "Let's watch tv", "Domenico watches tv"]
    tdidf = TdIdf("Domenico", "", documentList)
    result = tdidf.num_docs_containing_word("Domenico",documentList)
    assert_equal(2, result)

def test_term_frequency():
    word = "house"
    document = "I have a house. The house is red. I will open the windows and clean my house."
    tdidf = TdIdf("house", document, [])
    result = tdidf.tf(word, document) #it should be 0.038....
    assert_true(result > 0 and result < 1)