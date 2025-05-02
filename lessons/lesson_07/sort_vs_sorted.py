numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers) # Виведе: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]`
res = numbers.sort()  # res = None, але numbers буде відсортований

# print(numbers)


def new_rows_without_empty(list_of_rows):
    return [k for k in list_of_rows if len(k) > 0]

def update_rows_without_empty(list_of_rows):

    empty_indexes = []

    for index, k in enumerate(list_of_rows):
        if len(list_of_rows[index]) == 0:
            empty_indexes.append(index)

    for k in empty_indexes[::-1]:
        list_of_rows.pop(k)



my_rows = 'asd   asdasd   asd '.split(' ')
print(my_rows)
new_row = new_rows_without_empty(my_rows)
print(f'{"-"*80}\n{my_rows}\nnew rows = {new_row}')
print('-'*80)
update_rows_without_empty(my_rows)
print(f'my_rows = {my_rows}')