#!/usr/bin/python3

import pickle


class CustomObject:

    def __init__(self, name, age, is_student):

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is_student: {}".format(self.is_student))

    def serialize(self, filename):

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print("An error ocurred while serializing the object")
            return None

    @classmethod
    def deserialize(cls, filename):

        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print("An error ocurred while deserializing the object")
            return None
