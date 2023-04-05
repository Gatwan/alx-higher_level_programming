#!/usr/bin/python3
""" Displays response header value """
from requests import get
from sys import argv


if __name__ == "__main__":
    """ sends request to URL and displays header """
    r = get(argv[1])
    req_id = r.headers.get('X-Request-Id')
    print(req_id)
