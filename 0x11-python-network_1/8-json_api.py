#!/usr/bin/python3
""" Sends a POST request to URL with a letter as parameter """
from requests import post
from sys import argv


if __name__ == "__main__":
    """ Searches API """
    par = {'q': ""}
    try:
        par['q'] = argv[1]
    except Exception:
        pass

    r = post('http://0.0.0.0:5000/search_user', par)

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except Exception:
        print("Not a valid JSON")
