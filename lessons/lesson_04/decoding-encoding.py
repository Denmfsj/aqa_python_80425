
greetings_utf8 = 'Hello mr Pool'  # utf-8, default
greetings_win_1251 = greetings_utf8.encode('windows-1251')  # win-1251, перетворили
greetings_decode = greetings_win_1251.decode('windows-1251')  # повернули з win-1251 до utf-8

print(greetings_utf8)
print(greetings_win_1251)
print(greetings_decode)