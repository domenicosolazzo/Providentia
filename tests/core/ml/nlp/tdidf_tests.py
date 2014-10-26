from nose.tools import *
from providentia.core.ml.nlp.tdidf import TdIdf

def test_frequency_of_a_word:
    document = "abc abc abc ciao I am Domenico"
    word = "abc"
    tdidf = TdIdf(word, document, [])
    tdidf.freq()