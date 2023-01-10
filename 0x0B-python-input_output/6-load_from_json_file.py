#!/usr/bin/python3
"""Object from JSON file"""
import json


def load_from_json_file(filename):
    """Creates object"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
