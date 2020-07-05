import json

from fastapi import FastAPI

from app.models.person import Person
from app.services.person_service import PersonService

app = FastAPI()


@app.post('/new', status_code=201)
def new_person(person: Person):
    return PersonService().create_person(person)
