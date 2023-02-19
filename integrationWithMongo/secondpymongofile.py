import pprint
import pymongo as pyM
import datetime
import os
cliente = os.environ['cliente']

cliente = pyM.MongoClient(cliente)

db = cliente.test
posts = db.posts

# for post in posts.find():
#     pprint.pprint(post)

# print(posts.count_documents({}))

# print('ocorrências do autor mike')
# print(posts.count_documents({"author": "Mike"}))

# # procurar por meio das tags
# print(posts.count_documents({"tags": "insert"}))

# # encontrar documento com a tag insert
# pprint.pprint(posts.find_one({"tags": "insert"}))

# recuperando infos da coleção post de maneira coordenada
# for post in posts.find({}).sort("date"):
#     pprint.pprint(post)

# result = db.profiles.create_index([('author', pymongo.ASCENDING)],
#                                  unique=True)

# print(sorted(list(db.profiles.index_information())))

# user_profile_user = [
#     {'user_id': 211, 'name': 'Luke'},
#     {'user_id': 212, 'name': 'Joao'}]

# # insere novos documentos
# result = db.profile_user.insert_many(user_profile_user)

# lista de coleções armazenadas no mongodb test
print("coleções armazenadas no mongodb")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# remover coleção de documentos
# db['profile'].drop()

# deletar um documento que esteja no banco de dados através de um índice
# db.profile_user.delete_one({"name": "Luke"})

# # deletar varios documentos
# db.profile_user.delete_many({"name": "Luke"})

# deletar banco de dados
# cliente.drop_database('teste')
