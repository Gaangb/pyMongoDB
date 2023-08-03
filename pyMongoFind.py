import pymongo
import pymongo as pyM
import pprint

client = pyM.MongoClient("<cole aqui o link do seu banco de dados mongoDB do atlas")
db = client.test
posts = db.posts

print("\ndocs presentes na coleção")
for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({})) # Conta quantos documentos possuem no total
print(posts.count_documents({"author": "Gael"})) # conta quantos documentos com author gael possui
print(posts.count_documents({"tags": "insert"})) # conta quantos documentos com tags insert possui

print("\nRecuperando informações de maneira ordenada")

for post in posts.find({}).sort("author"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(db.profiles.index_information()))

print("\nColeções armazenadas no mongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)


"""""
print("\nverificando por author")
pprint.pprint(db.posts.find_one({"author": "Belinha"}))
"""""
