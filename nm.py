from pymongo import MongoClient
import json
from bson.objectid import ObjectId

client = MongoClient()

db = client['coin']

for i in db.bankTransactions.find({'_id': ObjectId('568ba29fe4b0d89496ae5f1e')}):
    print i


