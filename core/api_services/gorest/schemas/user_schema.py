from marshmallow import Schema, fields, validate, ValidationError

from core.api_services.gorest.enums.gender_enum import UserGenderEnum


class UserMarks(Schema):

    id = fields.Integer(required=True, strict=True)
    name = fields.Str(required=True)


def len_more_than_3(value):
    if len(value) < 4:
        raise ValidationError('Len must be more than 3 chars')

def is_first_is_capital(value):

    if value[0] != value[0].upper():
        raise ValidationError('First letter must be upper')



class UserSchema(Schema):
    #
    gender = fields.Enum(by_value=True, enum=UserGenderEnum, required=True)
    id = fields.Integer(required=True, strict=True, validate=validate.Range(min=1))
    name = fields.Str(required=True, validate=validate.And(len_more_than_3, is_first_is_capital))
    email = fields.Email(required=True)
    status = fields.Str(required=True, allow_none=True)


    # user_marks = fields.Nested(UserMarks)  # nested - вкладеність
    # some_field = fields.Raw(allow_none=True)  # може бути, а може і не бути, а може бути null, не перевіряти тип



data = [
    {'id': 55, 'name': 'Asasdasd',
     'email': 'somayaji_abhirath@klocko-ferry.example', 'gender': 'female', 'status': 'active'},
    {'id': 8002251, 'name': 'Amb. Lakshmidhar Varrier',
     'email': 'lakshmidhar_amb_varrier@little-yundt.test', 'gender': 'male', 'status': 'active'}
]

UserSchema(many=True).load(data)

# Enum

