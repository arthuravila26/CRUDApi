from fastapi import HTTPException


class PersonNotFound(HTTPException):
    def __init__(self, msg: str = 'Person not found.'):
        super().__init__(detail=msg, status_code=422)