import time   # бібліотека


quantity_of_requests = 1
time_between_requests = 0.1  # sec

time_of_wait = 10 # sec

# current_time = time.time()  # поверне кількість міктосекунд починаючи з 00:00 1.01.80
# while time.time() - current_time < time_of_wait:  #  поки не пройшло 60 секунд
#
#     print(f'{quantity_of_requests}, {time.time()} Sending request')
#
#     time.sleep(time_between_requests)  # чекати, нічого не робити
#     quantity_of_requests += 1  # збільшити лічільник зроблених запитів


# import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())