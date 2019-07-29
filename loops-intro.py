item = ""
while item != "quit":
    print("enter an item yo check the price: ")
    item = input()
    
    if item == "pizza":
        print("$3 per slice")
    elif item == "orange":
        print("$4")
    else:
        print("we dont have that")