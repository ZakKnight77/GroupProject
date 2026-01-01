import json


def get_game_data() -> dict:  # main func called to return game data dict
    data: dict = load_json_file("game_data.json")
    if is_game_data_valid(data):
        # return data only if it fits the structure
        return data
    return {}


def load_json_file(file_loc: str) -> dict:
    try:
        with open(file_loc, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                return {}  # saved data is not a dictionary
    except Exception as e:
        print(e)
        return {}


def is_game_data_valid(game_data: dict) -> bool:  # this returns bool for if the data is valid
    valid_room_data_keys: list[str] = ["description", "end_game", "items", "directions", "needed_item"]
    valid_item_data_keys: list[str] = ["description", "collectible"]

    if len(game_data) == 0:
        return True
    for room in game_data:
        if not isinstance(game_data[room], dict):
            print("Room data should be a dict")
            return False
        
        for room_key in game_data[room]:
            if not room_key in valid_room_data_keys:
                print(f"Room key {room_key} not valid")
                return False
            
        for item_val in game_data[room]["items"].values():
            if not isinstance(item_val, dict):
                print("Item data should be a dict")
                return False
            
            for item_key in item_val:
                if not item_key in valid_item_data_keys:
                    print(f"Item key {item_key} is not  valid")
                    return False
    return True

