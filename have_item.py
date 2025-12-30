def use_item(inventory, room_name, json_path="rooms.json"): #uses inventory array, imported room string and the json file to see what the req item is#

    #opens the json file to see rooms#
    with open(json_path, "r") as file:
        rooms = json.load(file) 

    required_item = rooms[room_name]["required_item"]

    #iterates through inventory#
    for item in inventory: 
        if item == required_item: 
            inventory.remove(item) #if continuing, gets rid of item from inventory#
            print(f"You used the {required_item}. You may move to the next room.")
            return

    print(f"You dont have the {required_item}. You can't continue.") 
    return 
