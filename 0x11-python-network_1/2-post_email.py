#!/usr/bin/python3
""" Displays the response of POST request to the passed URL """
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    """
    sends a POST request to the passed URL with email
    as the parameter
    """
    url = argv[1]
    email = argv[2]

    email_encode = urlencode({"email": email}).encode('utf-8')

    with urlopen(url, email_encode) as response:
        body = response.read().decode('utf-8')
        print(body)
