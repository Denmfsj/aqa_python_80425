bool([])
bool(dict())
bool(tuple())
bool(set())
bool(False)
bool(None)
bool(0)
bool(0.0)
bool('')


users_from_api = []

# if users_from_api:  # if bool(users_from_api) is True:
#     print('users list is NOT empty')
# else:
#     print('users list is empty')
#
# print('Done')


card_number = 1111222233334444
expected_card_number = 11112222333344441
cvv = 123
expected_cvv = 122
has_money = True

# print('Start')
# надіслати гроші
# if bool(card_number == 1111222233334444) and bool(cvv == 123) and bool(has_money):
# if card_number == expected_card_number and cvv == expected_cvv and has_money:
#     print('You data is correct you can sent money')
# elif cvv != expected_cvv:
#     print('cvv is incorrect')
# elif card_number != expected_card_number:
#     print('Card number is incorrect')
# else:
#     print('smth goes wrong')
# print('Done')


api_response = []
can_be_empty = True

# if api_response:
#     print('Checking response')
# elif can_be_empty:
#     # print('Response is empty and it can be')
#     pass
# else:
#     print('Error: response is empty')

# if api_response:
#     print('Checking response')
# else:
#     if can_be_empty:
#         # print('Response is empty and it can be')
#         pass
#     else:
#         print('Error: response is empty')
#
# if api_response:
#     print('Checking response')
# else:
#     if not can_be_empty:  #  not True => False
#         print('Error: response is empty')

# api_response = []
# can_be_empty = True
#
# # if bool(api_response) or bool(not api_response) and can_be_empty:
# # if (False) or bool(not False) and bool(True):
# # if (False) or (True) and (True):  => if (False or True) and True => True and True
# if api_response or not api_response and can_be_empty:
#     if api_response:
#         print('Checking response')
# else:
#     print('Error: response is empty')



