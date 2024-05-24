class VerboseList(list):

    def append(self, item):

        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):

        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):

        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, i=None):

        if i is None:
            del_item = super().pop()
            print("Popped [{}] from the list".format(del_item))
            return del_item
        else:
            del_item = super().pop(i)
            print("Popped [{}] from the list".format(del_item))
            return del_item
