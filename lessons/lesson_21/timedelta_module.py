from datetime import timedelta, datetime


datetime_row_2 = '21-05-2025 18:00:15.1548 -0500'  # TZ = UTC + 5 годин
datetime_row_3 = '20-05-2025 16:55:45.1548 -0500'  # TZ = UTC + 5 годин

datetime_dt_1 = datetime.strptime(datetime_row_2, '%d-%m-%Y %H:%M:%S.%f %z')
datetime_dt_3 = datetime.strptime(datetime_row_3, '%d-%m-%Y %H:%M:%S.%f %z')


datetime_dt_1_min_5_min = datetime_dt_1 + timedelta(seconds=-5*60)  # 5 хвилин

# print(datetime_dt_1)
# print(datetime_dt_1_min_5_min)

def get_time_with_diff(datetime_obj, **kwargs) -> datetime:
    return datetime_obj + timedelta(**kwargs)

# print(datetime_dt_1)
# print(get_time_with_diff(datetime_dt_1, days=-8))
# print(get_time_with_diff(datetime_dt_1, minutes=-8))

diff = datetime_dt_1 - datetime_dt_3
print(diff)
print(diff.total_seconds())
print(diff.seconds)
print(diff.days)