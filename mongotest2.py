import pymongo
client = pymongo.MongoClient("mongodb+srv://Sujit:<sujit1995>@Sujit.mq95dvg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d= {
    "name": "Sujit",
    "email":"sujitkumarpati02@gmai.com" ,
    "surname":"PATI"
}
db1 =client['mongotest']
coll =db1['test']
coll.insert_one(d)