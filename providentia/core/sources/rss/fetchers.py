from sources import DataSource
import feedparser

class Fetcher(object):
    __data_adapter = None

    def __init__(self):
        self.__data_adapter = DataSource.get_instance()

    def fetch_feeds(self):
        feed_list = []
        rss_list = self.__data_adapter.fetch_rss()
        for rss in rss_list:
            print(rss_list)
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


