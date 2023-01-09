#!/usr/bin/python3
""" Define class MyInt """


class MyInt(int):
    """ Inverts == and != """

    def __eq__(self, other):
        """ Changes == """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Changes != """
        return int(self) == int(other)
