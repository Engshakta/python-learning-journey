def greet(lang):
    if lang == "English":
        return "Hello"  # Returns value to the caller
    elif lang == "Somali":
        return "Iska waran"
    elif lang == "French":
        return "Bonjour"
    else:
        return "Salam"

# Now we call the function AND print what it returns
print(greet("English")) 
print(greet("Somali"))  
print(greet("Ahmaric"))
