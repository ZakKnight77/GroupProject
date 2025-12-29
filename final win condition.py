def check_if_end_game(game_state):
    # if endgame in the loaded json file is true, it will return the other function
    room = game_state.world[game_state.current_room]
    if room.get("end_game") is True:
        return end_game_handler
    return None  # if endgame is false, it wont show anything and not triggering the end game handler


def end_game_handler(): 
    print("You have reached the final moment.")
    choice = input("Choose win or lose: ").strip().lower()  # gives generic place holder option to win or lose

    losing_choices = {"lose"}  # creates variable for losing choices (open for multiple if needed), setting the losing choice

    if choice in losing_choices:  # goes through the losing choices variable to see if user input matches
        print("you lost.")
        return "lose"
    else:
        print("You win.")
        return "win"

    # Game ends here
