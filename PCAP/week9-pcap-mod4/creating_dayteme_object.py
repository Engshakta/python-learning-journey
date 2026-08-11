from datetime import datetime
my_watch = datetime(2026,7,15,15,30)
print(my_watch)

print(my_watch.date())
print(my_watch.time())

#  Methods that return the current date and time
photo_a = datetime.utcnow()
photo_b = datetime.now()

print(photo_a.tzinfo == photo_b.tzinfo)