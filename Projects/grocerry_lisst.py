groccery_list = []
print("This is your groccery list: ")

while True:
    item = input(("Please enter the groccery name or type done to finsh"))
    if item.lower() == 'done':
        break
    if not item:
        print("You cannot add an empty item")
        continue

    groccery_list.append(item)
    print(f"Added: {item}")



    
print(f"\nThe groccey list is: {groccery_list}")

