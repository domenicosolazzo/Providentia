from sources import DataSource
from providentia.core.models.document import FeedDocument
import feedparser

class Fetcher(object):
    __data_adapter = None

    def __init__(self):
        self.__data_adapter = DataSource.get_instance()

    def fetch_feeds(self):
        """
        Fetch information from a list of rss feeds
        :return: A list of feed
        """
        feed_list = []
        rss_list = self.__data_adapter.fetch_rss()
        for rss in rss_list:
            rss_href = rss.get('url', None)
            rss_title = rss.get('title', '-')
            if rss_href is not None:
                feed = feedparser.parse(rss_href)
                feed_list.append({
                    'title':rss_title,
                    'href':rss_href,
                    'status': feed.get('status', 400),
                    'updated': feed.get('updated', None),
                    'updated_parsed': feed.get('updated_parsed', None),
                    'encoding': feed.get('encoding', None),
                    'bozo': feed.get('bozo', None),
                    'headers': feed.get('headers', {}),
                    'etag': feed.get('etag', None),
                    'version': feed.get('version', None),
                    'entries': feed.get('entries', []),
                    'namespaces': feed.get('namespaces', None)
                })

        return feed_list

    def fetch_entries(self):
        """
        Fetch entries from a list of rss feed
        :return: A list of entries
        """
        entries = []
        rss_list = self.__data_adapter.fetch_rss()
        for rss in rss_list:
            rss_href = rss.get('url', None)
            if rss_href is not None:
                feed = feedparser.parse(rss_href)
                [entries.append(FeedDocument(entry.get('title', ''), entry.get('summary', ''))) for entry in feed.get('entries', [])]
        return entries



