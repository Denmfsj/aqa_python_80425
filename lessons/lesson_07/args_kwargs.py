# def multipl_sum(first, *args):
#     res = first
#     for k in args:
#         res += k
#
#     print(res)
#     return res
#
# # multipl_sum(1, 2)
#
# def greetings_polite(first_name, **kwargs):
#
#     polite_row = ''
#     for k in kwargs: # key in dict
#         polite_row += f'{k} of {kwargs[k]}, '
#
#     print(f'{first_name}\n{polite_row}')
#
# greetings_polite('Ilia', lord='Winterfall', son='Baldur')


# def set_registration_form(res_of_ui_form: str, **kwargs):
#
#     # reg_for_on_ui = ....
#
#     # всі поля на формі які було вказано
#     for key in kwargs:
#         reg_for_on_ui.find(key).fill(kwargs[key])
#
#
#
# # форма з 3ма полями
# def set_user_reg_form(user_name, user_pass, user_age):
#     set_registration_form(res_of_ui_form='http...', user_name=user_name, user_pass=user_pass, user_age=user_age)
#
# # форма з 4ма полями
# def set_investor_reg_form(user_name, user_pass, user_age, how_much_money_you_invest):
#     set_registration_form(res_of_ui_form='http...', user_name=user_name, user_pass=user_pass, user_age=user_age,
#                           how_much_money_you_invest=how_much_money_you_invest)
#
#
# def set_investor_reg_form(user_name, user_pass, user_age, how_much_money_you_invest):
#     set_registration_form(res_of_ui_form='http...',
#                           user_name=user_name, user_pass=user_pass, user_age=user_age,
#                           how_much_money_you_invest=how_much_money_you_invest, from_='from')


