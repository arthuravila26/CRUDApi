from pydantic import BaseModel
from pydantic.schema import datetime


class People(BaseModel):
    name: str
    age: int
    phone: str
    address: str
    register_date: datetime
