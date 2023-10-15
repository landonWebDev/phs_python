room_list = {
    "NW": {
        "visited": False,
        "monster": {
            "type": "Dragon",
            "hp": 50,
            "dmg_multiplier": 1.5,
        },
        "loot": [],
        "exits": {
            "south": "W",
            "east": "N"
        }
    },
    "N": {
        "visited": False,
        "loot": [],
        "exits": {
            "east": "NE",
            "south": "C",
            "west": "NW",
        }
    },
    "NE": {
        "visited": False,
        "loot": ["sword", "shield"],
        "exits": {
            "west": "N",
        }
    },
    "W": {
        "visited": False,
        "loot": [],
        "exits": {
            "north": "NW",
            "east": "C",
            "south": "SW",
        }

    },
    "C": {
        "visited": False,
        "loot": [],
        "exits": {
            "north": "N",
            "west": "W",
            "south": "S",
        }
    },
    "E": {
        "visited": False,
        "exit": True,
        "exits": {
            "south": "SE",
        }
    },
    "SW": {
        "visited": True,
        "exits": {
            "north": "W",
        }
    },
    "S": {
        "visited": False,
        "monster": {
            "type": "Skeleton",
            "hp": 10,
            "dmg_multiplier": 1.0,
        },
        "exits": {
            "north": "C",
            "east": "SE",
        }
    },
    "SE": {
        "visited": False,
        "monster": {
            "type": "Zombie",
            "hp": 10,
            "dmg_multiplier": 1.0,
        },
        "exits": {
            "north": "E",
            "west": "S",
        }
    },
}


def set_room_visited(room):
    room_list[room]["visited"] = True


def move_north(current):
    if 'north' in room_list[current]["exits"]:
        new_room = room_list[current]["exits"]["north"]
        # print('CURRENT ROOM UPDATED TO: ', current)
        return new_room
    else:
        return current


def move_east(current):
    if 'east' in room_list[current]["exits"]:
        new_room = room_list[current]["exits"]["east"]
        # print('CURRENT ROOM UPDATES TO: ', current)
        return new_room
    else:
        return current


def move_south(current):
    if 'south' in room_list[current]["exits"]:
        new_room = room_list[current]["exits"]["south"]
        # print('CURRENT ROOM UPDATES TO: ', current)
        return new_room
    else:
        return current


def move_west(current):
    if 'west' in room_list[current]["exits"]:
        new_room = room_list[current]["exits"]["west"]
        # print('CURRENT ROOM UPDATES TO: ', current)
        return new_room
    else:
        return current


# move_east()

# Loop over these actions until either you reach the exit
# Prompt to move character
# Move character
# If in exit, break from while loop and end game

# if/else chain
# (ignore for now) Handle loot (update multipliers or whatever for the loot you picked up)
# Handle empty room (tell user it's empty and move to next... continue while loop)
# Update global variables for monster (check monster type, update health/dmg, etc)
#   If combat, run the combat while loop until combat ends
