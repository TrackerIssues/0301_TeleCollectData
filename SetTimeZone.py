import datetime
from pytz import timezone, utc

# KST = timezone('Asia/Seoul')

now = datetime.datetime.utcnow()
# UTC 기준 naive datetime : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879)

utc.localize(now)
# UTC 기준 aware datetime : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879, tzinfo=<UTC>)


def NowDateTime(dtZone) :
    dtZone.localize(now)
    # UTC 시각, 시간대만 KST : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)
    dtDateTime = utc.localize(now).astimezone(dtZone)
    return dtDateTime