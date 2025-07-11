recursive_count = 0

def search(lst, target):
    try:
        global recursive_count
        recursive_count += 1
        target = int(target)

        if lst[0] == target:
            print(f"{target} found in  list.")
        else:
            if len(lst) > recursive_count:
                search(lst[recursive_count:], target)
            else:
                print(f"{target} not found in list. \nTry a different number.")
        search_has_ended = True
        return search_has_ended
    
    except ValueError:
        print("Enter a valid integer.")

number_list = [7, 44, 16, 37, 24, 6, 25, 30, 27, 49, 24, 43, 45, 37, 44, 44, 11, 8, 27, 11, 0, 5, 1, 2]

while True:    
    userChoice = input("\nEnter number to search: ")
    if search(number_list, userChoice):
        break