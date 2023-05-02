#!/usr/bin/python3
''' function that returns a python object '''

import json


def from_json_string(my_str):
    '''returns Python objects'''
    return json.loads(my_str)
