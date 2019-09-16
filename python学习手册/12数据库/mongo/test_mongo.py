import pymongo

mongo_url="127.0.0.1:27017"

client=pymongo.MongoClient(mongo_url)

database="myDatabase"
db=client[database]

collection="myCollection"
db_coll=db[collection]

queryArgs={'data':'2018-12-17'}
search_rs=db_coll.find(queryArgs).sort('age',-1)
for record in search_rs:
    print(f"_id = {record['_id']}, age = {record['age']}")