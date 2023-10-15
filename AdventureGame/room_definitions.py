room_list = {
    "NW": {
        "visited": False,
        "monster": {
            "type": "Dragon",
            "hp": 150,
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
            "hp": 100,
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
            "hp": 100,
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
