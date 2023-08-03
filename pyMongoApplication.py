import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("<cole o link do seu banco mongodb do atlas aqui>")

db = client.test
collection = db.test_collection
# print(db.test_collection)

# definicao a informação do arquivo do doc
post = {
    "author": "Gael",
    "text": "My first mongodb application",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id  # insere um objeto


# print(post_id)
# print(db.posts.find_one())
# pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [
    {
        "author": "Izzana",
        "text": "Another post",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.datetime.utcnow()},
    {
        "author": "Belinha",
        "text": "Post from Joao. New post available",
        "titulo": "Fun",
        "date": datetime.datetime.utcnow()}]

result = posts.insert_many(new_posts) # insere mais de um objeto

user_profile_user = [
    {'user_id': 211, 'name': 'Lulu'},
    {'user_id': 212, 'name': 'Jhony'}]

result = db.profile_user.insert_many(user_profile_user)

# print(result.inserted_ids)




