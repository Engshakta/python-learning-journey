from os import strerror
try:
    stream = open ("photo.jpg","wb")
except Exception as exc:
    print("failed becouse:", strerror(exc.errno))