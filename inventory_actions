#data from other peoples scripts (temporary for testing purposes)
current_room = "Room1" #placeholder
inventory = []
#I'm assuming the json data is stored as 'game_data' so it's written as such here
""""""

#FOR THOSE LOOKING THIS OVER- this will need to implement Nicoletas self.inventory thing but im not>
#>100% sure how it works? We'll have a meeting to resolve it + understand how the files can access each other

#I do not understand how to reference variables from other scripts overall. halp.

def AddItem(item):
        if (inventory.length == 5):
            return "Inventory full, choose an item to drop."
        else:  
            inventory.append(item)
        
        
def RemoveItem(item):
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
        
def PickUpItem(item):
        game_data[current_room[items]].remove(item)
        AddItem(item)
        
def DropItem(item, current_room):
    #May need to add UI display and user input to choose item to drop, if that isnt someone elses task already
    if (InventoryContains(item) == False):
        return (f"Cannot drop {item}, not in inventory.") #shouldn't happen if UI input works correctly
    RemoveItem(item)
    game_data[current_room[items]].append(item)
        

def InventoryContains(item):
    for index in inventory:
        if index == item:
            return True
    return False
