
def AddItem(inventory, item):
    '''Adds new item, max size of 5 (0-4)'''
    if (inventory.length == 5):
        return "Inventory full, choose an item to drop."
    else:  
        inventory.append(item)
        
        
def RemoveItem(inventory, item):
    '''Removes item from inventory, does nothing else with it'''
    if (inventory.length == 0):
        #Ideally this wont happen unless theres a mistake somewhere
        return "Inventory empty, nothing to remove."
    else:
        #Removes first instance of item found
        for index in inventory:
            if index == item:
                inventory.remove(index)
                break
            else:
                print(f"Attempted to remove {item} from inventory, could not be found.")
        
def PickUpItem(current_room, item):
    '''Removes target from the room and calls AddItem'''
    current_room[items].remove(item)
    AddItem(item)
        
def DropItem(current_room, item):
    '''Calls RemoveItem and put target into the current rooms list of items'''
    if (InventoryContains(item) == False):
        return (f"Cannot drop {item}, not in inventory.") #shouldn't happen if UI input works correctly
    RemoveItem(item)
    current_room[items].append(item)
        

def InventoryContains(inventory, itemname):
    '''Checks if item is in inventory, Item name passed is a string, not the item object'''
    for index in inventory:
        if index[0:itemname.len-1] == itemname:
            return True
    return False
