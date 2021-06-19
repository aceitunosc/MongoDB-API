from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, aacuser, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:28684/?authMechanism=DEFAULT&authSource=AAC' % (aacuser, password))
        self.database = self.client['AAC']

# creates new object with given data
    def create(self, data):
        if data is not None:
            try:           
                self.database.animals.insert_one(data)
                return True
            except PyMongoError:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
#reads object with given data
    def read(self, data=None):
        if data is None:
            return self.database.animals.find({})
        else:
            return self.database.animals.find(data)
#replace the object matching query and returns old object
    def update(self, query, data):
        if data is not None:
            try:
                return self.database.animals.find_one_and_replace(query, data, upsert=False)
            except PyMongoError as err:
                raise Exception("Error querying MongoDB: ", err)
        else:
            raise Exception("Nothing to update, because data parameter is None")
#deletes all objects matchting query and returns number of deleted objects
    def delete(self, data):
        if data is not None:
            res = self.database.animals.delete_many(data)
            return {"deleted_count": res.deleted_count}
        else:
            raise Exception("Nothing to delete, because data parameter is None")

client = AnimalShelter("aacuser", "kash2274")