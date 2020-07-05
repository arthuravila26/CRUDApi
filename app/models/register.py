from mongoengine import Document, StringField, IntField, queryset_manager


class Register(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    phone = StringField(required=True)
    address = StringField(required=True)

    meta = {
        'people': 'register',

    }

    @classmethod
    def create_person(cls):
        person = Register()
        return person


    @queryset_manager
    def get_by_name(doc_cls, queryset, name):
        return queryset(name=name).first()
