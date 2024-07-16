#!/usr/bin/env python3
'''This module provides a function to update topics in a MongoDB collection.

The update_topics function takes a MongoDB collection, a name, and a list of topics as input.
It updates all documents in the collection that match the given name, setting their topics to the provided list.
'''

def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
        name (str): The name to match documents against.
        topics (list): The list of topics to set.

    Returns:
        None
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    