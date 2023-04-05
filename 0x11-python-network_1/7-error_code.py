#!/usr/bin/python3
""" Displays the body of a URL response """
from requests import get
from sys import argv


if __name__ == "__main__":
    """ Prints HTTP status code (error) """
    r = get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
