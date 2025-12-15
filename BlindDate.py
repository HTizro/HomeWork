import datetime
import random
from datetime import timedelta

boys = ["ali", "hasan", "hamed"]
girls = ["sara", "zahra", "fatemeh"]

date_time = datetime.datetime.now()

for i in boys:
  j = random.randint(0, len(girls)-1)
  print(f"{i} and {girls[j]} in date {date_time.month}/{date_time.day}")
  girls.remove(girls[j])
  date_time += timedelta(days=10)
