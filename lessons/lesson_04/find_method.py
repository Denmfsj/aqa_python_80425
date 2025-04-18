# print(len('Методи'))
# print('Методи'[1:5:2])

row = ('Метод .find() використовується для пошуку підстрічки в рядку і повертає індекс першого'
       ' входження знайденої підстрічки. Якщо підстрічка не знайдена, Висновок: повертається -1.')

# print(row.find('т'))  # 2
# print(row.find('од'))  # 3
# print(row.find('М'))  # 0
# print(row.find('м'))  # -1
# print(row.find('asdasd'))  # -1


# print('find' in row)  # bool
# print(row.find('find'))  # поверне число

# if 'Висновок' in row:  # поверне True або False
#     all_sub_rows = row.split('Висновок') # список зі строкамию Із row вирізав 'Висновок' і записав в список
#     last_sub_row = all_sub_rows[-1]  # останній елемент списку, тобто все що йде після слова ВИсновок
#     len_of_last_sub_row = len(last_sub_row)
#     print(last_sub_row)
#     print(len_of_last_sub_row > 10)
#
# #
# #      # print(len(row.split('Висновок')[-1]) > 10)  # кількість символів після слова Висновок > 10
# # print('---------------')
# if row.find('Висновок') != -1:  # поверне число  і більше якщо слово є row і  поверне -1 якщо слова нема в row
#     first_index = row.find('Висновок')  # шукаю перше входження
#     print(first_index)
#     len_of_word = len('Висновок')
#     index_after_word = first_index + len_of_word
#     row_after_vus = row[index_after_word:]  # row[start:end:step], row[start:] тобто з start і до кінця печення
#     print(row_after_vus)
#     print(len(row_after_vus) > 10)


row = ('Метод .find() використовується для пошуку підстрічки  для в рядку і повертає індекс першого'
       ' входження знайденої підстрічки. Якщо підстрічка не знайдена, Висновок: повертається -1.')


# print(row.find('для'))  # 31
# print(row[row.find('для'):])
#
#
# find_start_with = row.find('для')
# index = row.find('для', row.find('для') + 1)
# # index = row.find('для', 32)
# print(row.find('для', row.find('для') + 1))
# print(row[index:])

print(row.find('для', 0, 34))  # не включаючі останній символ