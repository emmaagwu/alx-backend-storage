#!/usr/bin/env python3
'''This module contains a function to insert a new document in a MongoDB collection.
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        **kwargs: Keyword arguments representing the fields and values of the document.

    Returns:
        str: The inserted document's ID.

    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
