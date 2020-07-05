from datetime import datetime

from mongoengine import EmbeddedDocument, DateTimeField


class PersonUpdate(EmbeddedDocument):
    date_update = DateTimeField(required=True, default=datetime.now())
