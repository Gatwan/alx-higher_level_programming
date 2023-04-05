#!/usr/bin/python3
""" Displays the body of the response """
from requests import post
from sys import argv


if __name__ == "__main__":
    """ Sends a POST request to URL with email as a parameter """
    url = argv[1]
    email = argv[2]

    email_par = {"email": email}

    r = post(url, data=email_par)
    response = r.text
    print(response)
