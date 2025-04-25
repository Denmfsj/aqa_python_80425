

list_of_numbers = [1,2,3,4,5,10,5,2,5]

list_of_numbers.sort(reverse=True)

list_of_rows = 'jasgdlkj sf ajhf asf dk;lasjd adgf adlfh as;jl fa'.split()

print(list_of_rows)
# lambda x: len(x)
list_of_rows.sort(key=lambda x: len(x))  # сортування до довжині слова він мін до макс
list_of_rows.sort(key=lambda x: len(x), reverse=False)  # сортування до довжині слова він мін до макс
list_of_rows.sort(key=lambda x: len(x), reverse=True)  # сортування до довжині слова він макс до мін


list_of_values = [
    (1, ['aa', 55]),
    (2, ['cc', 77]),
    (3, ['hh', 89]),
    (4, ['bb', 12]),
    (5, ['dd', 5]),
]

# list_of_values.sort(
#     key=lambda x: x[1][1]
# )

sorted_list = sorted(list_of_values, key=lambda x: x[1][1])

print(list_of_values)
print(sorted_list)