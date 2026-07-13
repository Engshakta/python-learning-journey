from os import strerror
file_name = input("Enter the name of the file to analyse: ")
histogram = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

try:
    stream = open(file_name, "rt")

    for line in stream:
        for char in line:
            letter = char.lower()

            if letter in histogram:
                histogram[letter] += 1
    stream.close

    for letter in sorted(histogram.keys()):
        count = histogram[letter]
        if count > 0:
            print("f{letter} -> {count}")
    
except IOError as e:
    print("An I/O error occured", strerror(e.errno))