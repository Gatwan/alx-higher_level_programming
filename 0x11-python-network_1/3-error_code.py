#!/usr/bin/python3
""" Displays the body response of a URL request """
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    """ Manage HTTPError exceptions """
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
