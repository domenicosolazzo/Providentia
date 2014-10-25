from sources import DataSource

class Fetcher(object):
    __data_adapter = None

    def __init__(self):
        self.__data_adapter = DataSource.get_instance()

    def fetch_documents(self):
        rss_list = self.__data_adapter.fetch_rss()
        return rss_list
    

