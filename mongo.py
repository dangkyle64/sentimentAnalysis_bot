from pymongo import MongoClient

client = MongoClient("mongodb+srv://zachfaulkner02:$Greinke21@cluster0.x5robxp.mongodb.net/")
class mongo_():
    def insertData(textInput, textOutput):
        db = client["db"]
        collection = db["data"]
        doc = {"input": textInput, "output": textOutput}
        collection.insert_one(doc)

    









