"""
This file has functions for adding, removing, picking up, and dropping items.
"""

def AddItem(inventory: list, item: str) -> str:
    """Add an item to the inventory if it is not already present."""
    if item in inventory:
        return f"You have this {item} in your inventory"
    inventory.append(item)
    return f"This {item} has been added to your inventory"


def RemoveItem(inventory: list, item: str) -> str:
    """Remove an item from the inventory if it exists."""
    if item not in inventory:
        return f"This {item} is not in inventory"
    inventory.remove(item)
    return f"This {item} has been removed from inventory"


def PickUpItem(room: dict, inventory: list, item: str) -> str:
    """
    Attempt to pick up an item from the room.
    Only collectible items can be added to the inventory.
    """
    room_items = room.get("items", {})

    if not isinstance(room_items, dict):
        return "The item data should be a dict"

    # Case-insensitive matching 
    item_lower = item.lower()
    room_items_lower = {k.lower(): k for k in room_items.keys()}

    if item_lower not in room_items_lower:
        return f"{item} not in this room"

    actual_key = room_items_lower[item_lower]
    item_data = room_items[actual_key]

    # Non-collectible items cannot be picked up
    if not item_data.get("collectible", False):
        return f"This {actual_key} cannot be collected"

    add_result = AddItem(inventory, actual_key)

    # If item added this removes it from the room
    if "added to inventory" in add_result:
        del room_items[actual_key]

    return add_result


def DropItem(room: dict, inventory: list, item: str) -> str:
    """
    Drop an item from the inventory into the current room.
    Dropped items become collectible again.
    """
    room_items = room.get("items", {})

    if not isinstance(room_items, dict):
        return "Item data should be a dict"

    #  Case-insensitive matching for dropping
    item_lower = item.lower()
    inventory_lower = {i.lower(): i for i in inventory}

    if item_lower not in inventory_lower:
        return f"This {item} is not in inventory"

    actual_key = inventory_lower[item_lower]

    remove_result = RemoveItem(inventory, actual_key)

    if "removed from inventory" not in remove_result:
        return remove_result

    # Add dropped item back into the room
    room_items[actual_key] = {
        "description": f"{actual_key} dropped here",
        "collectible": True
    }

    return f"{actual_key} has been dropped"


def InventoryContains(inventory: list, item: str) -> bool:
    """Return True if the inventory contains the item."""
    return item in inventory
