my_list = [1,2,3,4,54, 45, 5]
my_tuple = (1,2,3,4,54, 888, 5)
my_text = ('Послідовність — це впорядкований контейнер елементів, проіндексованих цілими числами або хешами. '
           'Python має вбудовані типи послідовностей, відомі як рядки (байти або str),'
           ' кортежі, списки, набори та словники)')

# print(my_text[0])  # дай мені нульовий елемент
# print(my_text[1])  # дай мені перший елемент
# print(my_text[-1])  # дай мені останній елемент
# print(my_text[-2])  # дай мені перед останній елемент
# print(my_list[-2])  # дай мені перед останній елемент
# print(my_tuple[-2])  # дай мені перед останній елемент

# print(my_tuple[5555])  # дай мені неіснуючий
# print(my_tuple[-5556])  # дай мені неіснуючий

# [a:b:c]  a - початок, , - кінець, c - крок
# a = 0 by default, b - всі до кінця, c = 1 by default

first_15_chars = my_text[0:15]  # від 0 включно по 15 невключноб 15 елементів
print(first_15_chars)
print(len(first_15_chars))

first_15_chars_v2 = my_text[:15] # від 0 включно по 15 невключноб 15 елементів
until_last_15_chars =  my_text[:-15] # все крім сотанніх 15
print(until_last_15_chars)

each_2_sym = my_text[::2]  # кожний другий
print(each_2_sym)

revert_row= my_text[::-1]  # перегорнути строку
print(revert_row)

cut_middle =  my_text[:15] + my_text[-15:]  # перші 15 + останні 15
print(cut_middle)

cut_middle_with_step =  my_text[:15:2] + my_text[-15::3]
print(cut_middle_with_step)

# if text_a != text_b:
#     print(f'Texts are not the same\ntext_a: {text_a[:30]}\ntext_b: {text_b[:30]}')

half_of_text = my_text[:len(my_text)//2]
print(half_of_text)
print(my_list[::])