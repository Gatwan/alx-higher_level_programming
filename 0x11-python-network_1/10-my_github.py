#!/usr/bin/python3
""" Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id """
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(username, password))
    print(r.json().get('id'))
