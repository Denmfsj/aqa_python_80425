
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
row = 'Виведіть, скільки слів у тексті починається з Великої літери?'

print(row.split())
for word in row.split():  # row.split() - список слів, для кожного слова в цьому списку
    if word.istitle():
        print(word)


# # task 09
# """ Перевірте чи починається якесь речення з "By the time".
# """
#
# for sentence in adwentures_of_tom_sawer_sentences:
#     if ...:
#         print(True, 'Sentense start with "By the time"')



# names = ['alex', 'mixa', 'nic']
# ages = [20, 30, 40]
#
# print(list(zip(names, ages)))
# for k in zip(names, ages):
#     print(k)