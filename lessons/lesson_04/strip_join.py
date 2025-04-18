row = '  Методи asd ads   as dd 1  2   3  '

# print(row.rstrip())
# print(row.lstrip())
# print(row.strip())

# row_without_spaces = row.strip()
# print(row_without_spaces)
#
# list_of_words = row_without_spaces.split()
# print(list_of_words)
#
# row_with_1_space_between_words = ' '.join(list_of_words)
# print(row_with_1_space_between_words)
#
# print('_'.join(['1','2','3']))

row = '__Методи_asd_ads_'

print(row.strip('_').replace('_', ' '))
