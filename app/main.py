import json

from fastapi import FastAPI

from app.db.register import Register

app = FastAPI()

@app.post('/new')
def new_person(person):
    people = Register.objects.post(person=person)
    return json.loads(people)