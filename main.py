from tracking_game import GameState
from json_file_loader import get_game_data
from global_constants import DIRECTION_SUCCESS_CODE, DIRECTION_GAME_OVER_CODE, DIRECTION_MOVE_FAIL_CODE
## main program file


def main() -> None:
    game_data: dict = get_game_data()
    if game_data != {}:
        game_state: GameState = GameState(game_data, list(game_data.keys())[0])
        game_loop(game_state)


def game_loop(game_state: GameState) -> None:
    game_active: bool = True
    while game_active:
        print(game_state.look())
        # Take input here
        choice: list = ["choice code", "args..."]  # placeholder from when real input comes through Joshes script

        match choice[0].upper():  # converted to upper incase casing mistake
            case "DIRECTION":  # could be moved to global constants script
                game_active = get_move_room(game_state)
            case "VIEW_INV":
                print(game_state.show_inventory())
            case "PICK_ITEM":
                # choice [1] in this case should be a string item name
                if len(choice) >= 2:
                    game_state.pick_up(choice[1])
            case "DROP_ITEM":
                if len(choice) >= 2:
                    game_state.drop(choice[1])


def get_move_room(game_state: GameState) -> bool:  # returns bool if breaking game loop
    while True:
        # get input of chosen direction
        chosen_dir: str = input("Choose direction: ")  # placeholder?
        
        if chosen_dir.upper() == "BACK":
            return True  # indicate the the player doesnt want to move, go back to main

        move_value: tuple = game_state.move_to(chosen_dir)
        
        if move_value[1] == DIRECTION_SUCCESS_CODE:
            return True  # game continues in new room
        elif move_value[1] == DIRECTION_GAME_OVER_CODE:
            print(move_value[0])
            return False  # game is over
        elif move_value[1] == DIRECTION_MOVE_FAIL_CODE:
            print(move_value[0])
            # dont return here as loop can continue


if __name__ == "__main__":
     main()

