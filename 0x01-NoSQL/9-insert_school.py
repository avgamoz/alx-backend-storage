#!/usr/bin/bash python3
"""Inserts  a new document in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert a documents into a collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
