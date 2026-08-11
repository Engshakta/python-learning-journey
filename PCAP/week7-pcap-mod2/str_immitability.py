# You cannot use del to remove specific characters by index.
alphabet = "abcdefghijklmnopqrstuvwxyz"
del  alphabet[0] 

# Strings do not have an .append() method.
alphabet.append("A")

# Strings do not have an .insert() method.
alphabet.insert(0, "A")

""""Even though strings cannot be changed in place, 
you can simulate modification by creating a new string object 
and assigning it back to the same variable """

alphabet = "a" + alphabet 
alphabet = alphabet + "z"

print(alphabet)