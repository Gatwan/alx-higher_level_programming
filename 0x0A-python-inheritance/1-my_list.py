#!/usr/bin/python3
""" class that inherits from list """


class MyList(list):
    """ prints the list """

    def print_sorted(self):
        """ public instance method """
        print(sorted(self))
