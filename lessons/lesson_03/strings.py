# one_line_row = 'Це\tодинарний рядок.\nnew row\\'
#
# # {}
# greetings = 'Hello ... How are you ?'
#
# print(greetings)
# print('Hello Den How are you ?')
# greetings = 'Hello Ivan How are you ?'
# print(greetings)


#f'Hello {} How are you ?'  # f-string
# for name in ['Den', 'Alex', 'Ivan', 'Margo']:
#     print(f'perimeter is {20} + {40} = {20 + 40} ?')
#     print(f'Hello {name} How are you {{}} ?')
#     print(f'Hello', name, 'How are you {} ?')
#     print(f'Hello ' + name + ' How are you {} ?\n')

greeting = 'Hello {} How are you {{}}?'

print(greeting.format('Alex'))
print(greeting.format('Ivan'))

print("Привіт, %s!" % 'Den')


print(len('123'))
print(pow(5,2))
