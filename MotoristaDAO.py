from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nome: str, nota: int):
        try:
            resultado = self.db.collection.insert_one({"nome": nome, "nota": nota})
            print(f"Motorista criado com o id: {resultado.inserted_id}")
            return resultado.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            resultado = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {resultado}")
            return resultado
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None

    def update_motorista(self, id: str, nome: str, nota: int):
        try:
            resultado = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, "nota": nota}})
            print(f"Motorista atualizado: {resultado.modified_count} documento(s) modificado(s)")
            return resultado.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            resultado = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {resultado.deleted_count} documento(s) deletado(s)")
            return resultado.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
