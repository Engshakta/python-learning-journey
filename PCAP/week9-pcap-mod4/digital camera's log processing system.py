from os import strerror
try:
    stream = open("raw_log.txt", "rt")
    for line in stream:
        print(line, end = "")
    stream.close()
except IOError as exc:
    print("Failed to process logs:", strerror(exc))