from pymongo import MongoClient

client = MongoClient("mongodb+srv://zachfaulkner02:$Greinke21@cluster0.x5robxp.mongodb.net/")

db = client["db"]

collection = db["tuples"]

rec={

}

rec = db.myTable.insert(rec)



