

asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}

asn_to_class = {
    'Áhmed' : 'A',
    'Abdishakur' : 'B',
    'Khaalid' : 'C',
    'Omer' : 'D'
}

del asn_to_class['Omer']

print("After", len(asn_to_grade))

for assignment in asn_to_class:
    print(assignment)

asn_to_class ['Ai'] = 'E'

for assignment in asn_to_class:
    print(asn_to_class [assignment])

for assignment in asn_to_class:
    print(assignment , asn_to_class [assignment])


dictionary = {
    "name": "Ahmed",
    "age": 25,
    "email": "test@gmail.com"
}

dictionary ['phone number'] = '0933472410'

dictionary ['phone number'] = '0902089517'

dictionary.update({"status": "Active"})



dictionary.popitem()


for key in dictionary.keys():
    print(key, "->", dictionary[key])


for key in sorted(dictionary.keys()):
    print(key, " -> ", dictionary[key])


school_class = {}
while True:
    name = input("Enter the students's name:")
    if name == '':
        break
    score = int(input("Enter the student's score:"))
    if score not in range(0,11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":" , adding / counter)