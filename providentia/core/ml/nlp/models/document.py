class BasicDocument(object):
    def __init__(self):
        pass

class FeedDocument(object):
    title = ''
    description = ''

    def __init__(self, title, description):
        self.title = title
        self.description = description