
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, UTC

uri = "mongodb+srv://hhao9:gobadgers@cluster0.xi6gx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

print(client.list_database_names())

db = client.test 

print(db.list_collection_names())

book1 = {
	"name": "明朝那些事儿",
	"author": "当年明月",
	"category": ["历史", "文学"],
	"status": "读完",
	"rate": 4.5,
    "date": datetime.now(UTC)
}

books = db.books 

# result = books.insert_one(book1)

book2 = [
    {
	"name": "把时间当作朋友",
	"author": "李笑来",
	"category": "励志",
	"status": "读完",
	"rate": 4.5
    },
    {
	"name": "财富自由之路",
	"author": "李笑来",
	"category": "励志",
	"status": "在读",
	"rate": 4.5
    }
]

# result = books.insert_many(book2)

# result = books.find_one({"author": "李笑来"})

result = books.find_one({"author": "李笑来", "status": "在读"})

result = books.find_one({"category": "文学"})

from bson.objectid import ObjectId

result = books.find_one({"_id": ObjectId("66da20b8e9ef016fe33bb4bb")})

print(result)

result = books.find({"author": "李笑来"})

print(list(result))

# note that after having used this result, you can no longer access it. 
# Try printing it twice and you'll see that it will only print once. 

print(books.count_documents({"author": "李笑来"}))

# result = books.delete_one({"_id": ObjectId("66da20b8e9ef016fe33bb4bb")})

result = books.update_one({"name": "财富自由之路"}, {"$set": {"status": "读完"}})

