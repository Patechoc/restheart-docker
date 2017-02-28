#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" 
  Reminder PyMongo
"""

import os, sys
import logging
from pprint import pprint
import argparse
import time
import datetime
import pandas as pd
from pymongo import MongoClient


    
def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='main.log',level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p')
    test_mongo()
    test_RESTHeart()


    
def test_mongo():
    ## create a MongoClient to the running mongodb instance
    client = MongoClient('localhost', 27017)

    ## create/get a database
    db = client['test-database']

    ## (lazily) create/get a collection 
    collection = db['test-collection']

    ## Insert one document
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id

    ## Find one document
    print db.collection_names(include_system_collections=False)
    pprint(posts.find_one())
    pprint(posts.find_one({"_id": post_id}))

    ## Insert multiple messages
    new_posts = [{"author": "Mike",
                  "text": "Another post!",
                  "tags": ["bulk", "insert"],
                  "date": datetime.datetime(2009, 11, 12, 11, 14)},
                 {"author": "Eliot",
                  "title": "MongoDB is fun",
                  "text": "and pretty easy too!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    result = posts.insert_many(new_posts)
    pprint(result.inserted_ids)

    ## Find all documents that match a given query
    

    ## Find all documents that match a given query
    
    
    
def test_RESTHeart():
    pass
    
    
if __name__ == "__main__":
    main()

