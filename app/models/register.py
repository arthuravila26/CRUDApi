from uuid import uuid4

from mongoengine import Document, StringField, IntField, queryset_manager, Q


class Register(Document):
    id = StringField(required=True, primary_key=True)
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

    def get_all_people(self):
        return Register.objects().all()

    def get_all_names(cls, name, age):
        return Register.objects(Q(name=name) & Q(age=age))

    def get_bet_age(cls, final_age, initial_age):
        return Register.objects(Q(age__gte=initial_age) & Q(age_lte=final_age)).all().count()

    @queryset_manager
    def get_by_id(doc_cls, queryset, id):
        return queryset(id=id).first()

    #return Register.objects(Q(name=name) & Q(age=age)) para fazer uma query no mongo