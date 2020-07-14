import json
from datetime import datetime
from uuid import uuid4

from app.db.mongo_init import Mongo
from app.models.person import Person
from app.models.register import Register
from app.utils.exceptions import PersonNotFound
from app.utils.logger import logger


class PersonService:
    def __init__(self):
        self.mongo = Mongo()

    def create_person(self, data: Person):
        person = Register.create_person()
        person.id = str(uuid4())
        person.name = data.name
        person.age = data.age
        person.phone = data.phone
        person.address = data.address
        person.save()
        logger.info(f'Person {data.name} has been registered.')
        return self.serialize(person)

    def get_everybody(self):
        people_json = [self.serialize(people) for people in Register().get_all_people()]
        return people_json

    def serialize(self, data):
        return {
            "id": str(data.id),
            "name": data.name,
            "age": data.age,
            "phone": data.phone,
            "address": data.address
        }

    def get_all_names(self, name):
        try:
            name_person = Register.get_by_name(name)
            return self.serialize(name_person)
        except:
            raise PersonNotFound()

    def person_update(self, data, name):
        person = Register.get_by_name(name)
        Register.objects(name=name).update(
            set__name=data.name,
            set__age=data.age,
            set__phone=data.phone,
            set__address=data.address
        )
        person.reload()
        return json.loads(person.to_json())

    def delete_person(self, id):
        Register.get_by_id(id)
        Register.objects(id=id).delete()
        return f'The person has been deleted at {datetime.now()}'
