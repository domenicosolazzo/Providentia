from sources import DataSource
import feedparser

class Fetcher(object):
    __data_adapter = None

    def __init__(self):
        self.__data_adapter = DataSource.get_instance()

    def fetch_documents(self):
        feed_list = []
        rss_list = self.__data_adapter.fetch_rss()
        for rss in rss_list:
            rss_url = rss.get('url', None)
            rss_title = rss.get('title', '-')
            if rss_url is not None:
                feed = feedparser.parse(rss_url)
                feed_list.append({'title':rss_title, "feed": feed})

        return feed_list


