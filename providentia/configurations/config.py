import os

class ConfigurationManager(object):
    def __init__(self):
        pass
    @property
    def NUMBER_KEYWORDS(self):
        return int(os.environ.get('WINSDOM_NUMBER_KEYWORDS', 4))

    @property
    def HIERARCHICAL_CLUSTERING_T(self):
        return float(os.environ.get('HIERARCHICAL_CLUSTERING_T', 0.8))

    @property
    def HIERARCHICAL_CLUSTERING_IMAGE(self):
        return os.environ.get('HIERARCHICAL_CLUSTERING_IMAGE', 'hcluster.png')

    @property
    def HIERARCHICAL_CLUSTERING_DPI(self):
        return int(os.environ.get('HIERARCHICAL_CLUSTERING_DPI', 800))

    @property
    def RSS_DATA_SOURCE_TYPE(self):
        return os.environ.get('RSS_DATA_SOURCE_TYPE', "JSON")

