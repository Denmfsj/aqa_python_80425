
users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': True},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': True},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': True},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': True},
    {'id': 7, 'name': 'Anna', 'age': 20, 'job': False},
    {'id': 8, 'name': 'Maria', 'age': 20, 'job': True},
    {'id': 9, 'name': 'Inna', 'age': 20, 'job': True},
]

# дізнатись імена всіх працючих людей молодше 60
# якщо вік менше 60 і нема роботи = waringn
# якщо вік менше 60 і є робота = ОК
# якщо вік більше дорівнює 60 пропускаємо
# якщо id > 7 то пропускаємо

# for user in users:
#
#     #     if user.get('age') < 60:
#     #         if user.get('id') < 8:
#     #             if user.get('job') is True:
#     #                 print(f'{user["name"]} - OK')
#     #             else:
#     #                 print(f'{user["name"]} - waringn')
#
#
#     # continue  - піди в початок поточного циклу і візьми наступне значення
#     #  break - розриває цикл
#
#     # requirement 1
#     if user.get('age') >= 60:
#         continue  # пропуск роботи з юзером, перехід в наступну ітерацію цикла
#
#     # requirement 2
#     if user.get('id') > 7:
#         break  # виходжу з цикла
#
#
#     if user.get('job') is True:
#         print(f'{user["name"]} - OK')
#     else:
#         print(f'{user["name"]} - waringn')
#
# print('Done')


# for number in range(1, 11):  # for number in (1,2,3,4, 5,6,7,8,9,10)
#
#     if number %2 == 0:
#         continue
#     # виводити тільки для непарних
#     for number_2 in range(5, 100): # for number_2 in (5,6,7,8,9)
#         if number_2 > 9:
#             break
#
#         if number_2 % 2 == 1:
#             continue
#         # для парних
#         print(f'{number}*{number_2}={number*number_2}')


# for k in range(5):
#     print(k)
#     if k == 10:
#         break
# else:  # буде спрацьовувати якщо break не був викликаний в списку
#     print('The list want stopped')
