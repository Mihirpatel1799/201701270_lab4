from pymongo import MongoClient
from pprint import pprint
client=MongoClient("mongodb+srv://201701270:201701270@mihir-mwo9a.mongodb.net/test?retryWrites=true&w=majority")
db=client["analytics"]

agr = [
       {"$lookup" : {
            "from" : "accounts",
            "localField" : "accounts",
            "foreignField" : "account_id",
            "as" : "output"
        }},
       {"$unwind":"$output"},
        {"$match":{"output.products":"Commodity"}},
        {"$group":{"_id": "$username","avgAmount":  {"$avg": "$output.limit"}}}
       ]

val = db.customers.aggregate(agr)

for v in val:
    pprint(v)
