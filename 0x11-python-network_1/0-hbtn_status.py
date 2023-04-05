#!/usr/bin/python3
""" python script that fetches https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen


if __name__ == "__main__":
    """ prevents execution of import """
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        """ opens url and reads content """
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
