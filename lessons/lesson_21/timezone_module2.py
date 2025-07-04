from datetime import datetime
import pytz
from tzlocal import get_localzone


datetime_row_1 = '21-05-2025 18:00:15.1548'  # UTC, коли не вказано іншого
datetime_row_2 = '21-05-2025 18:00:15.1548 -0500'  # TZ = UTC + 5 годин
datetime_row_3 = '21-05-2025 18:00:15.1548 +0000'  # UTC,


datetime_dt_1 = datetime.strptime(datetime_row_1, '%d-%m-%Y %H:%M:%S.%f')  #  псевдо UTC, тут нема інформації про tomezone

# додати інформації про TZ
local_tz = str(get_localzone())

# додаємо цю TZ до часу
datetime_dt_1_local_tz = pytz.timezone(local_tz).localize(datetime_dt_1)
datetime_dt_1_utc_tz = pytz.timezone('UTC').localize(datetime_dt_1)

print(datetime_dt_1_local_tz)
print(datetime_dt_1_utc_tz)

diff = datetime_dt_1_utc_tz - datetime_dt_1_local_tz
time_int_utc = datetime_dt_1_local_tz - diff

