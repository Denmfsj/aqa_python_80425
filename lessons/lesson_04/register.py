row = '''Перевірка Регістру
Перевірка, чи рядок складається тільки з великих літер:'''

lower_case = row.lower()
upper_case = row.upper()
first_in_upper_case = row.capitalize()
each_first_in_upper_case = row.title()

print(lower_case) #  все маленькими
print(upper_case) #  все великими
print(first_in_upper_case) #   Перша буква велика, всі інші малі
print(each_first_in_upper_case) #   Перша буква кожного слова велика, всі інші малі
# print(row)

# row = 'hey .. 555 USD asdasd'  # usd, Usd, USD
#
# print(' usd ' in row.lower())
#
# user_name == user_name.title()

# lower_case = row.lower()
# upper_case = row.upper()
# first_in_upper_case = row.capitalize()
#
# print(row.islower())  # чи row == row.lower()
# print(row.isupper())  # чи row == row.upper()
# print(row.istitle())  # чи row == row.title()
# 
# print('12222'.isdigit())  # True  число в строці
# print('1a'.isdigit())  # False число в строці

