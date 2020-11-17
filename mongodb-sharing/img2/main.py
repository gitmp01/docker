#! /usr/bin/env python3
from pymongo import MongoClient

import time

def main():
    time.sleep(10)

    client = MongoClient("mongo", 27017)

    db = client.archive
    documents = db.documents

    print("Document found: {}", documents.find_one({"_id": "doc-1"}))

if __name__ == '__main__':
    main()