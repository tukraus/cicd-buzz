import os
import pymongo

def _get_db_host():
    db_host = os.getenv('DATABASE_HOST')
    if db_host is None:
        db_host = 'localhost'
    return db_host

def _get_db_client():
    return pymongo.MongoClient(_get_db_host(), 27017, tz_aware=True)['cicdbuzz']

def save_buzz(new_buzz):
    db = _get_db_client()
    return db['buzz'].insert_one({'buzz': new_buzz})

def get_all_buzzes() :
    db = _get_db_client()
    result = ''
    for s in db['buzz'].find():
        result += s['buzz'] + '\n'
    return result