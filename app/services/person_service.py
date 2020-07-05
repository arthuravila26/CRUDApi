import json

from app.db.mongo_init import Mongo
from app.models.person import Person
from app.models.register import Register
from app.utils.logger import logger


class PersonService:
    def __init__(self):
        self.mongo = Mongo()

    def create_person(self, data: Person):
        person = Register.create_person()
        person.name = data.name
        person.age = data.age
        person.phone = data.phone
        person.address = data.address
        person.save()
        logger.info(f'Person {data.name} has been registered.')
        return json.loads(person.to_json())
