import pprint

import pymongo as pyM
import datetime
import os
# cria a conexão com banco de dados
cliente = os.environ['cliente']

cliente = pyM.MongoClient(cliente)

# cria o banco de dados no mongodb
db = cliente.test
collection = db.test_collection

print(db.teste_collection)

# definição de info para compor o documento
post = {
    "author": 'Mike',
    "text": "My first mongofb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}
# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

pprint.pprint(db.posts.find_one())

# bulk inserts
# definição de infos para compor os documentos
new_posts = [{
    "author": 'Mike',
    "text": "Another post",
    "tags": ["bulker", "post", "insert"],
    "date": datetime.datetime.utcnow()

},
    {
        "author": 'Joao',
        "text": "Post for Joao. New post Available",
        "title": "Mongo is fun",
        "date": datetime.datetime(2009, 11, 10, 10, 45)}]

# inserir vários documentos no mongodb
result = posts.insert_many(new_posts)
print(result.inserted_ids)

# print('\n Recuperação final')
# pprint.pprint(db.posts.find_one({"author": "Joao"}))


# print('\n Documentos presentes na coleção posts')
# for post in posts.find():
#     pprint.pprint(post)


