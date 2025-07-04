from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def get_datetime_from_str(datetime_str, format='%d-%m-%Y %H:%M:%S'):
        return datetime.strptime(datetime_str, format)


datetime_row_1 = '21-05-2025 18:00:15.1548'  # UTC, коли не вказано іншого
datetime_row_2 = '21-05-2025 18:00:15.1548 -0500'  # TZ = UTC + 5 годин
datetime_row_3 = '21-05-2025 18:00:15.1548 +0000'  # UTC,



datetime_dt_1 = datetime.strptime(datetime_row_1, '%d-%m-%Y %H:%M:%S.%f')  #  всевдо UTC, тут нема інформації про tomezone
datetime_dt_2 = datetime.strptime(datetime_row_2, '%d-%m-%Y %H:%M:%S.%f %z')  #  UTC - 5 годин
datetime_row_3 = datetime.strptime(datetime_row_3, '%d-%m-%Y %H:%M:%S.%f %z')  #  UTC


print(datetime_dt_1)
print(datetime_dt_2)
print(datetime_row_3)
print(datetime_dt_2 - datetime_row_3)