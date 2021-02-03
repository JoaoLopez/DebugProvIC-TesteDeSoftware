import json
import sys
import os

def create_json(new_data = dict()):
    with open(name_json(), "w", encoding='utf-8') as json_file:
        json.dump(new_data, json_file, ident=4)

def add_node_to_json(nodo):
    try:
        with open(name_json, 'r', encoding='utf-8') as json_file:
            my_json = json.load(json_file)
    except IOError:
        create_json()
        my_json = dict()

    my_json[nodo['ev_id']] = nodo 
    create_json(my_json)

def name_json():
    return f"{sys.argv[0][:-3]}.json"