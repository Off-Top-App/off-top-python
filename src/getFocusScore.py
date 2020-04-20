from pymongo import MongoClient

def getAverageScore(collection):

    summedFS = 0
    for doc in collection.find():
        summedFS += int(doc["focus_score"])

    return(summedFS/collection.count()) #.count() is deprecated





mongo_client = MongoClient("mongodb+srv://off-top-dev:offtop123@cluster0-ci5ku.gcp.mongodb.net/off-top-db")

col = mongo_client["off-top-db"].sessions
score = getAverageScore(col)
print(score)