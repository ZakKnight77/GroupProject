"""
This is the entry point for the text adventure game. It loads game data, creates the GameState, and runs the main game loop.
"""

from tracking_game import GameState
from json_file_loader import get_game_data
from global_constants import (
    DIRECTION_SUCCESS_CODE,
    DIRECTION_GAME_OVER_CODE,
    DIRECTION_MOVE_FAIL_CODE,
)


def main() -> None:
    """Initialises the game and starts the game loop."""
    game_data: dict = get_game_data()

    if game_data != {}:
        # The first room from the JSON is the starting room.
        start_room = list(game_data.keys())[0]
        game_state: GameState = GameState(game_data, start_room)
        game_loop(game_state)


def game_loop(game_state: GameState) -> None:
    """Main loop that processes player input until the game ends."""
    game_active: bool = True

    print("Type 'help' for a list of commands.")

    while game_active:
        # This shows the room description 
        print("\n" + game_state.look())

        raw = input("> ").strip()

        if raw == "":
            print("Please enter a command.")
            continue

        # This is the input which is separeted into command and arguments
        parts = raw.split()
        command = parts[0].upper()
        args = parts[1:]

        match command:

            case "GO" | "MOVE" | "DIRECTION":
                if len(args) == 0:
                    print("Specify a direction.")
                else:
                    game_active = handle_move(game_state, args[0])

            case "PICK" | "GET" | "PICK_ITEM":
                if len(args) == 0:
                    print("Specify an item to pick up.")
                else:
                    print(game_state.pick_up(args[0]))

            case "DROP" | "DROP_ITEM":
                if len(args) == 0:
                    print("Specify an item to drop.")
                else:
                    print(game_state.drop(args[0]))

            case "VIEW_INV" | "INVENTORY":
                print(game_state.show_inventory())

            case "LOOK":
                print(game_state.look())

            case "HELP":
                print_help()

            case "QUIT" | "EXIT":
                print("Exiting game.")
                game_active = False

            case _:
                print("Unknown command.")


def handle_move(game_state: GameState, direction: str) -> bool:
    """
    This handles the movement and checks whether the game should continue.
    Returns True to keep playing and False to end the game.
    """
    message, status = game_state.move_to(direction)

    if status == DIRECTION_SUCCESS_CODE:
        return True

    elif status == DIRECTION_GAME_OVER_CODE:
        print(message)
        return False

    elif status == DIRECTION_MOVE_FAIL_CODE:
        print(message)
        return True

    return True


def print_help() -> None:
    """Displays the available player commands."""
    print(
        "Available commands:\n"
        "  go <direction>     - Move (also: move, direction). Example: go north\n"
        "  pick <item>        - Pick up an item (also: get). Example: get key\n"
        "  drop <item>        - Drop an item\n"
        "  inventory          - View your inventory\n"
        "  look               - Look around the room\n"
        "  help               - Show this help message\n"
        "  quit               - Exit the game"
    )


if __name__ == "__main__":
    main()



