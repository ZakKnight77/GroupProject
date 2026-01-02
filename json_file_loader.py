"""
This loads the game_data.json file and validates its structure before use.
"""

import json


def get_game_data() -> dict:
    """Load and validate game data from JSON."""
    data = load_json_file("game_data.json")
    if is_game_data_valid(data):
        return data
    return {}


def load_json_file(file_loc: str) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.
    """
    try:
        with open(file_loc, "r") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except Exception as e:
        print(e)
        return {}


def is_game_data_valid(game_data: dict) -> bool:
    """
    Validates the structure of the game world JSON.
    Ensures rooms, items, and directions follow the expected format.
    """
    valid_room_keys = {"description", "end_game", "items", "directions", "needed_item"}
    valid_item_keys = {"description", "collectible"}

    if not isinstance(game_data, dict):
        print("Game data should be a dictionary")
        return False

    if len(game_data) == 0:
        return True  

    for room_name, room_data in game_data.items():

        if not isinstance(room_data, dict):
            print("Room data should be a dict")
            return False

        # Checks room keys
        room_keys = set(room_data.keys())
        if not room_keys.issubset(valid_room_keys):
            for key in room_keys - valid_room_keys:
                print(f"Room key {key} not valid")
            return False

        # Checks the required keys for every room
        required = {"description", "end_game", "items", "directions"}
        if not required.issubset(room_keys):
            missing = required - room_keys
            for key in missing:
                print(f"Room key {key} not valid")
            return False

        # This validate room fields
        if not isinstance(room_data["description"], str):
            print("Room description must be a string")
            return False

        if not isinstance(room_data["end_game"], bool):
            print("end_game must be a boolean")
            return False

        if "needed_item" in room_data and not isinstance(room_data["needed_item"], str):
            print("needed_item must be a string")
            return False

        # This validate items
        items = room_data["items"]
        if not isinstance(items, dict):
            print("Item data should be a dict")
            return False

        for item_name, item_data in items.items():
            if not isinstance(item_data, dict):
                print("Item data should be a dict")
                return False

            item_keys = set(item_data.keys())
            if not item_keys.issubset(valid_item_keys):
                for key in item_keys - valid_item_keys:
                    print(f"Item key {key} is not valid")
                return False

            if not isinstance(item_data["description"], str):
                print("Item description must be a string")
                return False

            if not isinstance(item_data["collectible"], bool):
                print("collectible must be a boolean")
                return False

        # Validates directions
        directions = room_data["directions"]
        if not isinstance(directions, dict):
            print("Directions must be a dict")
            return False

        for direction, target_room in directions.items():
            if not isinstance(direction, str) or not isinstance(target_room, str):
                print("Directions must map strings to strings")
                return False

            if target_room not in game_data:
                print(f"Room key {target_room} not valid")
                return False

    return True



