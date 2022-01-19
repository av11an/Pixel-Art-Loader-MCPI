import pickle

class Pixelart:
    def __init__(self, name, length, width, ar):
        self.name = name
        self.length = length
        self.width = width
        self.ar = ar

    def set_size(self, length, width):
        self.length = length
        self.width = width

    def get_size(self):
        return self.length, self.width

    def set_array(self, ar):
        self.ar = ar

    def get_array(self):
        return self.ar

    def __str__(self):
        return '\n{} has a length and width of {}, with an array code of {}.'.format(self.name, self.get_size(),
                                                                                     self.get_array())
