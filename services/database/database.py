from pymongo import MongoClient
from services.database.interface_database import InterfaceDatabase


class Database(InterfaceDatabase):
    def __init__(self, host, port, database_name, collection_name):
        self.host = host
        self.port = port
        self.database_name = database_name
        self.collection_name = collection_name
        self._client = MongoClient(host=self.host, port=self.port)
        self._database = self._client[database_name]
        self._collection = self._database[collection_name]

    @property
    def collection(self):
        return self._collection

    @property
    def database(self):
        return self._database

    @property
    def client(self):
        return self._client
