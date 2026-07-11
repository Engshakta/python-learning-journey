def make_capsule(message):
    def robot():
        print("Capusle contains:", message)
    return robot

my_capsule = make_capsule("Secret Code 123")
my_capsule()