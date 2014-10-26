from nose.tools import *
from providentia.core.ml.nlp.utilities.document_utilities import DocumentHelper

def test_words_longer_than():
    words_list = ["ciao", "domenico", "a", "b", "123"]
    final_list = DocumentHelper.words_longer_than(words_list, 1)
    assert_true(isinstance(final_list, list))
    assert_true(len(final_list)==3)

def test_words_longer_than_raises_exception_if_input_is_not_a_list():
    assert_raises(Exception, DocumentHelper.words_longer_than, {}, 1)
    assert_raises(Exception, DocumentHelper.words_longer_than, True, 1)
    assert_raises(Exception, DocumentHelper.words_longer_than, 100, 1)

def test_wordpunct_tokenize():
    document = "This is a document"
    tokens = DocumentHelper.wordpunct_tokenize(document)
    assert_true(isinstance(tokens, list))
    assert_true(len(tokens) == 4)

def test_remove_html_markup():
    document = "<div>This is a document</div>"
    result = DocumentHelper.remove_html_markup(document)
    assert_equal("This is a document", result)
