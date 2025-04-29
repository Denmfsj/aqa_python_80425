#

# for k in range(10):
#     print('Sending request')
#     response = {}
#     # уявимо, що на 7й раз прийшла не порожня відповідь
#     if k == 7:
#         response = {'id': 5}
#
#     print(f'{k} has response {response}\n')
#     if response:
#         break


attempt = 0  #  спроба
while True:  # while condition

    print('While Sending request')
    response = {}
    # уявимо, що на 7й раз прийшла не порожня відповідь
    if attempt == 7:
        response = {'id': 5}

    print(f'{attempt} has response {response}\n')
    if response:
        break
    attempt += 1
