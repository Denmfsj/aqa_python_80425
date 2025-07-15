from enum import Enum


class UserGenderEnum(Enum):

    MALE = 'male'
    FEMALE = 'female'


# import pytest
# print(UserGenderEnum.FEMALE.value)
#
#
# class UIColumns(Enum):
#
#     USER_ID = 'user_id'
#     NAME = 'name'
#     CREATED_AT = 'created_on'
#     UPDATED_AT = 'updated_at'
#
#
# @pytest.mark.parametrize('column', list(UIColumns))
# def test_sorting(column):
#     print(f'Send request ith sort_by: {column.value}')