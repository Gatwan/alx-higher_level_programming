#!/usr/bin/python3
""" Displays response header value """
import requests
from sys import argv


if __name__ == "__main__":
    """ sends request to URL and displays header """
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
