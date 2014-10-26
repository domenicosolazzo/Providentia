
class DocumentHelper(object):
    def __init__(self):
        pass

    def words_longer_than(self, words_list, length):
        if not isinstance(words_list, list):
            raise Exception("The words_list must be a list")

        return [word for word in words_list if len(word) > length]