from nose.tools import *
from providentia.core.ml.nlp.tdidf import TdIdf

def test_frequency_of_a_word():
    document = "abc abc abc ciao I am Domenico"
    word = "abc"
    tdidf = TdIdf(word, document, [])
    result = tdidf.frequency()
    assert_equal(3, result)

def test_word_count():
    document = "I am Domenico"
    tdidf = TdIdf("", document, [])
    result = tdidf.wordcount()
    assert_equal(13, result)