#!/usr/bin/python3
""" Displays response header value """
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    """ Opens url and displays header value """
    with urlopen(argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
