# r - read, читати
# w - write, створювати і писати в
# a - append,  доповнювати/ствоювати i писати в

# with open('some_file.txt') as f:  # r by default
# with open('some_file.txt', 'r') as f:  # r by default


# list_of_words = ['apple', 'nabana', 'asdasd']
#
# with open(r'some_file.txt', 'w') as f:  # w -  створити і записати. Переписати якщо файл існує
#     f.write('some first for')
#
# with open(r'some_file.txt', 'a') as f:  # w -  доповнити існуючій, або створти якщо його нема і записати
#     f.write('\nsome second for')
#     f.write('\n')
#     f.write(str(list_of_words))
#     f.write('\n')
#
#     # запишу слова зі списка через пробіл
#     for k in list_of_words:
#         f.write(f'{k} ')
#     f.write('\n')
#     # запишу слова зі списка через |
#     f.write('|'.join(list_of_words))


with open(r'some_file.txt') as f:
    data = f.read()

print(data)