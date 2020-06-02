from mongoengine import Document, StringField, IntField, queryset_manager


class Register(Document):
    name: StringField(required=True)
    age: IntField(required=True)
    phone: StringField(required=True)
    address: StringField(required=True)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    @queryset_manager
    def get_by_name(doc_cls, queryset, person):
        person = queryset(person=person).first()

    meta = {
        'name': 'name',
    }
