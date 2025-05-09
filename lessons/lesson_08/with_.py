
# file = open('text.txt')  # створилил об'єкт
# data = file.read()  # вивичтали
#
# file.close()  # "закрили" файл


try:
    file_1 = None
    file_1 = open('text.txt')  # створилил об'єкт file_1
    data = file_1.read()  # вивичтали

    print(data)

finally:
    if file_1:
        file_1.close()


print('-'*80)

with open('text.txt') as file_2:   # створилил об'єкт file_2
    data2 = file_2.read()

print(data2)
print('done')




