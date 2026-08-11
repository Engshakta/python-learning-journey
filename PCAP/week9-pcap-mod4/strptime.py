from datetime import datetime

date_str = "2026/07/19 08:30:00"

dt_object = datetime.strptime(date_str,"%Y/%m/%d %H:%M:%S")

print(type(dt_object))
print(dt_object.year)