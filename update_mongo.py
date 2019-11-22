import pandas as pd
from pymongo import MongoClient


def read_data():
    return pd.read_csv('/home/martoso/Desktop/update_mongo.csv')


def create_json(df):
    query = []
    for idx, row in df.iterrows():
        find = str(row["id"])
        query_set = str(row["type"])
        query.append(find + ', ' + query_set)
    return query


def connection_mongo():
    client = MongoClient(
        'mongodb://infra_recorder:Nosql2018@192.168.26.181:27017/japeto')
    db = client.japeto
    collection = db.stations
    return collection


def insert_data(conn, documents):
    for document in documents:
        new_document = document.split(', ')
        result = conn.update_one({'_id': int(new_document[0])},
                                 {'$set': {"type": str(new_document[1])}})
    return print('Done')


data = read_data()
data = create_json(data)
conn = connection_mongo()
insert_data(conn, data)
