#!/usr/bin/python3
"""function that creates an Object from a “JSON file0"""
import json


def load_from_json_file(filename):
    """Create  Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
