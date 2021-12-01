import os


class MongoConfigs:
    MONGO_URI = os.getenv('MONGO_URI')

    def __init__(self):
        self.validate_mongo()

    def validate_mongo(self):
        if self.MONGO_URI is None:
            raise ValueError("MONGO_URI cannot be empty.")
