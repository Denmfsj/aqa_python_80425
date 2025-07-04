import time

# start_time = time.time()  # кількість секунд і мілісекунд починаючи в 1970
# # time.sleep(2.5)  # зупнить виконання на 2.5 секунди
# print(time.time() - start_time)
# print(time.time())
#
# import datetime

# print(datetime.datetime.fromtimestamp(1751646093.9387465))

print(time.localtime())
print(time.localtime().tm_mday)
print(time.localtime().tm_min)
print(time.localtime().tm_hour)
print(time.localtime().tm_wday)

def get_current_month():
    return time.localtime().tm_mon