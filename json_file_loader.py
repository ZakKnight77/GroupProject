import json


def get_game_data(file_loc: str) -> dict:  # main func called to return game data dict
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
