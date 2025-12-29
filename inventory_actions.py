def AddItem(inventory, item):
    '''Adds new item, max size of 5 (0-4)'''
    if len(inventory) == 5:
        return "Inventory full, choose an item to drop."
    else:  
        inventory.append(item)
        return f"{item} added to inventory."
        
        
def RemoveItem(inventory, item):
    '''Removes item from inventory, does nothing else with it'''
    if len(inventory) == 0:
        #Ideally this wont happen unless theres a mistake somewhere
        return "Inventory empty, nothing to remove."
    else:
        #Removes first instance of item found
        if item in inventory:
            inventory.remove(item)
            return f"{item} removed from inventory."
        else:
            print(f"Attempted to remove {item} from inventory, could not be found.")
            return f"{item} not found in inventory."
        
        
def PickUpItem(current_room, inventory, item):
    '''Removes target from the room and calls AddItem'''
    room_items = current_room.get("items", {})

    if item not in room_items:
        return f"{item} is not in this room."

    del room_items[item]

    return AddItem(inventory, item)
        
        
def DropItem(current_room, inventory, item):
    '''Calls RemoveItem and put target into the current rooms list of items'''
    if InventoryContains(inventory, item) == False:
        return (f"Cannot drop {item}, not in inventory.") #shouldn't happen if UI input works correctly
    
    RemoveItem(inventory, item)

    current_room.setdefault("items", {})

    current_room["items"][item] = {"description": f"A dropped {item}", "collectible": True}

    return f"You dropped {item}."
        

def InventoryContains(inventory, itemname):
    '''Checks if item is in inventory, Item name passed is a string, not the item object'''
    return itemname in inventory
