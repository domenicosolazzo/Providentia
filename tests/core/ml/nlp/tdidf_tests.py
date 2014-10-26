from nose.tools import *
from providentia.core.ml.nlp.tdidf import TfIdf

def test_frequency_of_a_word():
    document = "abc abc abc ciao I am Domenico"
    word = "abc"
    tfidf = TfIdf(word, document, [])
    result = tfidf.frequency(word, document)
    assert_equal(3, result)

def test_word_count():
    document = "I am Domenico"
    tfidf = TfIdf("", document, [])
    result = tfidf.word_count(document)
    assert_equal(13, result)

def test_num_docs_containing_word():
    documentList = ["I am Domenico", "Let's watch tv", "Domenico watches tv"]
    tfidf = TfIdf("Domenico", "", documentList)
    result = tfidf.num_docs_containing_word("Domenico",documentList)
    assert_equal(2, result)

def test_term_frequency():
    word = "house"
    document = "I have a house. The house is red. I will open the windows and clean my house."
    tfidf = TfIdf("house", document, [])
    result = tfidf.tf(word, document) #it should be 0.038....
    assert_true(result > 0 and result < 1)

def test_idf():
    word = 'city'
    document_list = ["I have a house", "This is another document", "yet another document", "My house is blue"]
    tfidf = TfIdf(word, "", document_list)
    result = tfidf.idf(word, document_list) # It should be 1.x
    assert_true(result > 1)

def test_calculate_tfidf():
    word = 'city'
    document_list = ["I have a house", "This is another document", "yet another document", "My house is blue"]
    document = "My house is outside the city"
    tfidf =TfIdf(word, document, document_list)
    result = tfidf.calculate() # It should be around 0.049
    print(result)
    assert_true(result > 0.049)



