#Recommended to use python try-except block to perform error handling.
from pprint import pprint
#use pprint instead of print to clearly print output documents
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
connectionString="mongodb+srv://201701270:201701270@mihir-mwo9a.mongodb.net/test?retryWrites=true&w=majority"
client=MongoClient(connectionString)
db=client["201701270"]
mycol=db["Sales_rep"]

try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')

except OperationFailure:
    print('wrong credentials')

else:
    print('connected to database')
    val = db.Sales.aggregate([
                {"$unwind" : {"path" : "$items"}},
                {"$group" : {
                        "_id" : "$items.name",
                        "sales_history" : {"$push" : {"storeLocation" : "$storeLocation","quantity" : {"$multiply" : ["$items.price","$items.quantity"]}}}
                            }
                },
                #{"$out" : "stock_replenish"}
            ])
    for v in val:
        mycol.insert_one(v)

finally:
	client.close()
