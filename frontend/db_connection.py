import pymongo

url = 'mongodb+srv://zachfaulkner02:$Greinke21@cluster0.x5robxp.mongodb.net/'
client = pymongo.MongoClient(url)  # connect to MongoDB

db = client["SentimentDB"]