class CountedIterator:

    def __init__(self, item):

        self.__iterator = iter(item)
        self.__counter = 0

    def __next__(self,):

        try:

            self.__counter += 1
            next_item = next(self.__iterator)
            return next_item
        except StopIteration:

            raise StopIteration

    def get_count(self):

        return self.__counter
