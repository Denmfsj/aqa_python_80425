
def is_empty_row(row):
    return len(row) > 0


my_descr = 'My name a A is  Den'.split(' ')
# print(my_descr)

print(list(filter(is_empty_row, my_descr)))
print(list(filter(lambda row: len(row) > 2, my_descr)))

print(sorted(my_descr))
print(sorted(my_descr, key=lambda x: len(x)))