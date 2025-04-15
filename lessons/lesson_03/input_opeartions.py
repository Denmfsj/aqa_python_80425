user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))  # '' якщо нічогоне ввести і натиснути  enter, то в змінну запишеться порoжня строка

print(f'Your name is { "mr/ms " + user_name}')
print(f'your age is {user_age - 1}')

# 'asd,as'.split(',')

# tpl = (1,2,3, 'asd', (1,'2222'), None, True, 5.25)
# lst = [1,2,3, 'asd', (1,'2222'), None, True, 5.25, [1,2,3]]