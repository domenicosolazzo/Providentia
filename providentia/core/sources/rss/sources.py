import feedparser
import os
import json

class DataSource(object):
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        data_source_type = os.environ.get('RSS_DATA_SOURCE_TYPE', "JSON")
        if data_source_type == "JSON":
            return RssJSONSource()
        else:
            raise Exception("Data source is not available")

    def fetch_rss(self):
        raise Exception("Not implemented")

class RssJSONSource(DataSource):
    """
    Extract data from json files
    """
    def __init__(self):
        super(RssJSONSource, self).__init__()

    def fetch_rss(self):
        rss_file = '%s/data/rss.json' % (os.path.dirname(os.path.realpath(__file__)))
        try:
            with open(rss_file) as f:
                rss_json = json.load(f)
                return rss_json.get('data', {})
        except:
            raise Exception("Rss not found")
