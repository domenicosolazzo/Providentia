from nose.tools import *
from providentia.core.sources.rss.fetchers import Fetcher

def test_fetcher():
    f = Fetcher()
    document_list = f.fetch_feeds()
    assert_true(document_list is not None)