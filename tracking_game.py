import json

class GameState:
    def __init__(self, world: dict, start_room: str="Room1"):
        self.world = world
        self.current_room = start_room
        self.inventory = []
    
    def get_current_room(self) -> str:
        """Current room"""
        return self.current_room
    
    def move_to(self, direction: str) -> str:
        room = self.world[self.current_room]
        exits = room.get("directions", {})
        if direction not in exits:
            return "You cannot go that way"

        next_room = exits[direction]
        target = self.world[next_room]
        needed_item = target.get("needed_item", "")

        if needed_item:
            if needed_item in self.inventory:
                self.current_room = next_room
            else:
                if needed_item in room.get("items", {}) and not room["items"][needed_item]["collectible"]:
                    self.current_room = next_room
                else:
                    return f"The item that is required is {needed_item} to proceed to {next_room}"
        else:
            self.current_room = next_room

        if target.get("end_game", False):
            return f"{target['description']} (Game over)"

        return f"In {next_room}"

    def get_item(self, item: str) -> str:
        """Pick up an item"""
        room = self.world[self.current_room]
        items = room.get("items", {})
        if item not in items:
            return f"There is no {item} here"
        if not items[item].get("collectible", False):
            return f"You cannot collect this {item}"
        self.inventory.append(item)
        del items[item]
        return f"{item} has been picked up"
    
    def drop_item(self, item: str) -> str:
        """Drop an item"""
        if item not in self.inventory:
            return f"{item} not here"
        self.inventory.remove(item)
        self.world[self.current_room].setdefault("items", {})[item] = {
            "description": "Dropped item",
            "collectible": True
        }
        return f"{item} has been dropped"
    
    def look(self) -> str:
        """Describe current room"""
        room = self.world[self.current_room]
        desc = room.get("description", "")
        items = room.get("items", {})
        item_list = ",".join(items.keys()) if items else "empty"
        exits = room.get("directions", {})
        exit_list = ",".join(exits.keys()) if exits else "none"
        return f"{desc}\nItems are: {item_list}\nExits: {exit_list}"
    
    def show_inventory(self) -> str:
        """Show inventory"""
        return "Inventory-" + (",".join(self.inventory) if self.inventory else "empty")
