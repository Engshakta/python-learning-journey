from os import strerror
try:
    
    src = open("source.jpg", "rb")

    dst = open("backup.jpg", "wb")


    buffer = bytearray(4096)


    bytes_read = src.readinto(buffer)
    while bytes_read > 0:
        dst.write(buffer[:bytes_read])
        bytes_read = src.readinto(buffer)
    
    src.close()
    dst.close()
    print("File copied successfully!")

except IOError as e:
    print("An I/O error occured:", strerror(e.errno))