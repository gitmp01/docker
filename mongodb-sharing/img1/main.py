#! /usr/bin/env python3

from pymongo import MongoClient
import time

def main():

    # wainting for mongod to start up
    time.sleep(5)

    client = MongoClient("mongo", 27017)

    db = client.archive
    documents = db.documents

    data = { "_id": "doc-1", "author": "Master Foo", "date": "2019-01-20" }

    id = documents.insert_one(data).inserted_id

    print(f'Document inserted id: {id}')

if __name__ == '__main__':
    main()