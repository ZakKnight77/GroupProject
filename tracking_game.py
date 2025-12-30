from global_constants import (
    DIRECTION_GAME_OVER_CODE,
    DIRECTION_MOVE_FAIL_CODE,
    DIRECTION_SUCCESS_CODE,
)
from inventory_actions import AddItem, RemoveItem, PickUpItem, DropItem, InventoryContains


class GameState:
    def __init__(self, world: dict, start_room: str = "Room1"):
        self.world = world
        self.current_room = start_room
        self.inventory = []

    def get_current_room(self) -> str:
        """Current room"""
        return self.current_room

    def move_to(self, direction: str) -> tuple:
        """
        Attempts to move the player in the given direction.
        Returns (message: str, status_code: int).
        """
        room = self.world.get(self.current_room)
        if room is None or not isinstance(room, dict):
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        exits = room.get("directions", {})
        if not isinstance(exits, dict):
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        if direction not in exits:
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        next_room_name = exits[direction]

        target = self.world.get(next_room_name)
        if target is None or not isinstance(target, dict):
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        needed_item = target.get("needed_item", "")

        if needed_item:
            if self.has_item(needed_item):
                self.current_room = next_room_name
            else:
                room_items = room.get("items", {})
                if (
                    isinstance(room_items, dict)
                    and needed_item in room_items
                    and not room_items[needed_item].get("collectible", True)
                ):
                    self.current_room = next_room_name
                else:
                    return (
                        f"The item that is required is {needed_item} to proceed to {next_room_name}",
                        DIRECTION_MOVE_FAIL_CODE,
                    )
        else:
            self.current_room = next_room_name

        if bool(target.get("end_game", False)):
            return f"{target.get('description', '')} (Game over)", DIRECTION_GAME_OVER_CODE

        return f"In {next_room_name}", DIRECTION_SUCCESS_CODE

    def look(self) -> str:
        """
        Returns a description of the current room, items, and exits.
        Text preserved exactly as you wrote it.
        """
        room = self.world.get(self.current_room, {})
        desc = room.get("description", "")

        items = room.get("items", {})
        if isinstance(items, dict) and items:
            item_list = ",".join(items.keys())
        else:
            item_list = "empty"

        exits = room.get("directions", {})
        if isinstance(exits, dict) and exits:
            exit_list = ",".join(exits.keys())
        else:
            exit_list = "none"

        return f"{desc}\nItems are: {item_list}\nExits: {exit_list}"

    def show_inventory(self) -> str:
        return "Inventory- " + (",".join(self.inventory) if self.inventory else "empty")

    def add_item(self, item):
        return AddItem(self.inventory, item)

    def remove_item(self, item):
        return RemoveItem(self.inventory, item)

    def pick_up(self, item):
        room = self.world.get(self.current_room, {})
        return PickUpItem(room, self.inventory, item)

    def drop(self, item):
        room = self.world.get(self.current_room, {})
        return DropItem(room, self.inventory, item)

    def has_item(self, item):
        return InventoryContains(self.inventory, item)


