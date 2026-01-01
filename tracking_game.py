"""
This handles the player movement, inventory actions, and room logic for the game engine.
"""

from global_constants import (
    DIRECTION_GAME_OVER_CODE,
    DIRECTION_MOVE_FAIL_CODE,
    DIRECTION_SUCCESS_CODE,
)
from inventory_actions import AddItem, RemoveItem, PickUpItem, DropItem, InventoryContains


class GameState:
    """Tracks the player's current room, inventory, and handles game logic."""

    def __init__(self, world: dict, start_room: str = "Room1"):
        self.world = world
        self.current_room = start_room
        self.inventory = []

    def get_current_room(self) -> str:
        """Returns the player's current room name."""
        return self.current_room

    def move_to(self, direction: str) -> tuple:
        """
        Attempts to move the player in the given direction.
        Returns (message, status_code).
        """
        room = self.world.get(self.current_room)
        if room is None or not isinstance(room, dict):
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        exits = room.get("directions", {})
        if direction not in exits:
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        next_room_name = exits[direction]
        target = self.world.get(next_room_name)

        if target is None:
            return "You cannot go that way", DIRECTION_MOVE_FAIL_CODE

        needed_item = target.get("needed_item", "")

        # Handle rooms that require an item
        if needed_item:
            if self.has_item(needed_item):
                self.current_room = next_room_name
            else:
                room_items = room.get("items", {})
                # Allow entry if the required item is in the room and non‑collectible
                if (
                    isinstance(room_items, dict)
                    and needed_item in room_items
                    and not room_items[needed_item].get("collectible", True)
                ):
                    self.current_room = next_room_name
                else:
                    return (
                        f"The item that is required is {needed_item} to proceed to {next_room_name}\n"
                        f"Another room may have the item that you need in order to continue",
                        DIRECTION_MOVE_FAIL_CODE,
                    )
        else:
            self.current_room = next_room_name

        # End‑game room
        if target.get("end_game", False):
            return f"{target.get('description', '')} (Game over)", DIRECTION_GAME_OVER_CODE

        return f"In {next_room_name}", DIRECTION_SUCCESS_CODE

    def look(self) -> str:
        """Returns the room description, items, and exits."""
        room = self.world.get(self.current_room, {})
        desc = room.get("description", "")

        items = room.get("items", {})
        item_list = ",".join(items.keys()) if items else "empty"

        exits = room.get("directions", {})
        exit_list = ",".join(exits.keys()) if exits else "none"

        return f"{desc}\nItems are: {item_list}\nExits: {exit_list}"

    def show_inventory(self) -> str:
        """Returns a formatted inventory list."""
        return "Inventory- " + (",".join(self.inventory) if self.inventory else "empty")

    # Inventory wrappers

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
        """Checks if the player has a specific item."""
        return InventoryContains(self.inventory, item)




