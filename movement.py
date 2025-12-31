import json
key = False

def room_1():
    print("""\nyou see three doors which door do you want to go through?
            1. Go through the left door choice 1
            2. Go through the middle door choice 2
            3. Go through the right door choice 3""")
    choice = input("Choose a door (1, 2, or 3): ")
    if choice == '1':
        print("\nYou chose the left door.")
        room_2()
    elif choice == '2':
        print("\nYou chose the middle door.")
        room_3()
    elif choice == '3':
        print("\nYou chose the right door.")
        room_4()
    else:
        print("\nInvalid choice. Please choose again.")
        room_1()

def room_2():
    print("\nYou enter a room the left door and get killed by a trap")

    print("do you want to restart? (yes/no)")
    restart = input().lower()
    if restart == 'yes':
        room_1()
    else:
        print("Game Over.")

def room_3():
    while True:
        print("""\nYou enter a room the middle door and see some items on a table
              you see a key to open a door.""")
    #items code here
        leave = input("Do you want to leave the room? (yes/no): ")
        if leave.lower() == 'yes':  
            room_1()
            break
        else:
            print("You decided to stay in the room.")

def room_4():
    print("\nYou enter a room the right door and find the door is locked and needs a key.")
    if key == False:
        print("You don't have the key to open the door.")
        room_1()
    elif key == True:
        print("You use the key to open the door and escape. You win!")

room_1()