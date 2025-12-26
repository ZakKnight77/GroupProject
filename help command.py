#Function to run help command#
def Help_command(room_name, rooms):
    if room_name not in rooms:
        print(f"Room '{room_name}' does not exist.") #check if room exists, catches fails and ends the function
        return

    room = rooms[room_name]

    #gives user room description#
    print(f"\n{room_name}")
    print("-" * len(room_name)) #purely aesthetic, creates seperation line, can be removed for uniformity with other's code
    print(room["description"]) 

    #gives user info on what needed items they need#
    needed_item = room.get("needed_item", "")
    if needed_item:
        print(f"\nYou need {needed_item} to proceed.")
    else:
        print("\nNo items are needed to proceed.")

    #gives user info on what items are in the room#
    if room["items"]:
        print("\nItems in the room:")
        for item_name, item_data in room["items"].items():
            print(f"- {item_name}: {item_data['description']}")
    else:
        print("\nThere are no items here for you to collect in this room.")

    #gives user info on directions#
    if room["directions"]:
        print("\nDirections you can take and where they lead:")
        for direction, destination in room["directions"].items():
            print(f"- {direction}: {destination}")
    else:
        print("\nThere are no exits, if you want to go back, choose the oposite direction of the way you came.")