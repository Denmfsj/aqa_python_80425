
numbers = [1,2,3,4]
my_row = 'asdasd'
my_dict = {1:2, 3:4}

# for k in my_dict:
#     print(k)



# for k in numbers:
#     print(k)


# list_a = ['a', 'c']
# list_a_interator = iter(list_a)  # list_a.__iter__()
# print(next(list_a_interator))  # list_a_interator.__next__()

# number_interator = iter(numbers)  # number_interator це об'єкт ітератора
# print(next(number_interator))  # надрукує 1 об'єкт
# print(next(number_interator))  # надрукує 2 об'єкт
# print(next(number_interator))  # надрукує 3 об'єкт
# print(next(number_interator))  # надрукує 4 об'єкт
# print(next(number_interator))  # надрукує 5 об'єкт

number_interator = iter(numbers)
while True:
    try:
        print(next(number_interator))
    except StopIteration:
        break

# for k in numbers:
#     print(k)
