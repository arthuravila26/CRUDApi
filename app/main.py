import json

from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.models.person import Person
from app.services.person_service import PersonService

app = FastAPI()


@app.post('/new', status_code=201)
def new_person(person: Person):
    return PersonService().create_person(person)


@app.get('/people', status_code=200)
def get_all_people():
    return PersonService().get_everybody()


@app.get('/{name}', status_code=200)
def get_all_names(name):
    return JSONResponse(PersonService().get_all_names(name))


@app.patch('/{name}', status_code=200)
def update_person(data: Person, name):
    return PersonService().person_update(data, name)


@app.delete('/{id}', status_code=200)
def delete_person(id):
    return PersonService().delete_person(id)
