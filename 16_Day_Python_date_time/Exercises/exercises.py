from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print("1-2:", f"{month}/{day}/{year}, {hour}/{minute}/{now.second}")

today = "5 December, 2019"
print("3:", datetime.strptime(today, "%d %B, %Y"))

# dont need timedelta
new_year = datetime(now.year + 1, 1, 1)
print("4:", new_year - now)

new_year_1970 = datetime(1970, 1, 1)
print("5:", now - new_year_1970) # wow
