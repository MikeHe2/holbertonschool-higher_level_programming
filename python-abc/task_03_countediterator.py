class CountedIterator:

    def __init__(self, item):

        self.__iterator = iter(item)
        self.__counter = 0

    def __next__(self,):

        next_item = next(self.__iterator)
        self.__counter += 1
        return next_item

    def get_count(self):

        return self.__counter
