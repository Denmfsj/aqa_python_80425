from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def get_datetime_from_str(datetime_str, format='%d-%m-%Y %H:%M:%S'):
        return datetime.strptime(datetime_str, format)


datetime_row_1 = '21-05-2025 18:00:15'
datetime_row_2 = '04-25-2025 18:00:15'
datetime_row_3 = '04-25-2025 18:00:15.555'
datetime_row_4 = '04-25-2025 4:00:15 PM'
datetime_row_5 = '25-07-30 11:00:15.12354 AM'
datetime_row_6 = '25 sep 15'


# dt_6 = datetime.strptime(datetime_row_6, '%y %b %d')
# print(dt_6)
#
# print(datetime.now())  # поточний дата+час
#
# datetime_dt_1 = datetime.strptime(datetime_row_1, '%d-%m-%Y %H:%M:%S')
# datetime_dt_2 = datetime.strptime(datetime_row_2, '%m-%d-%Y %H:%M:%S')
# datetime_dt_3 = datetime.strptime(datetime_row_3, '%m-%d-%Y %H:%M:%S.%f')
# datetime_dt_4 = datetime.strptime(datetime_row_4, '%m-%d-%Y %I:%M:%S %p')
# datetime_dt_5 = datetime.strptime(datetime_row_5, '%y-%m-%d %I:%M:%S.%f %p')
#
# example_dt = datetime.strptime('28/02/1000T18:00:15', '%d/%m/%YT%H:%M:%S')
# print(example_dt)  # str(example_dt)
# # day - mount - year
# example_dt_row = example_dt.strftime('%d-%m-%Y')
# print(example_dt_row)

# iso
print(datetime.fromisoformat('1000-02-28 18:00:15'))



