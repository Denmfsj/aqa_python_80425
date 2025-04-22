row = """Метод .replace() використовується для заміни входжень певної підстрічки іншою підстрічкою в рядку."""


new_row = row.replace('е', 'Е')
print(new_row)
print(row)

new_row_2 = row[:10] + '|' + row[11:]
print(new_row_2)

# print(row.replace('е', 'салат', 2))

row = '1, two, 1, four'

# new_row = row.replace('1', 'one', 1)
# print(new_row.replace('1', 'three'))

print(row.replace('1', 'one', 1).replace('1', 'three').replace('three', 'potato'))





new_row = row.replace('1', 'one')
print(new_row)
print(row.replace('1', 'one'))

