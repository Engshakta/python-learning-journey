import os 
def find (path, dir_name):
    try:
        abs_path = os.path.abspath(path)
        for item in os.listdir(abs_path):
            full_item_path = os.path.join(abs_path, item)
            if os.path.isdir(full_item_path):
                if item == dir_name:
                    print(full_item_path)
                    find(full_item_path, dir_name)
    except FileNotFoundError:
        print(f" the starting path ' {path}' was not found.")
