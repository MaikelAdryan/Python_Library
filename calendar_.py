import calendar
from datetime import datetime

YEAR = datetime.today().year
MONTH = datetime.today().month

print(calendar.month(YEAR, MONTH))
