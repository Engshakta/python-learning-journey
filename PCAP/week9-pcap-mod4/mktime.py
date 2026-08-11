import time
original_timestamp =1572879180.0
gmt_struct = time.gmtime(original_timestamp)
print(gmt_struct)
new_timestamp = time.mktime(gmt_struct)
print(new_timestamp)

print(original_timestamp == new_timestamp)