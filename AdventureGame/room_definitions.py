room_list = {
    "(1,3)": {
        "visited": False,
        "monster": {
            "type": "Dragon",
            "hp": 150,
            "dmg_multiplier": 1.5,
        },
        "loot": {
            "Widow Maker": {
            "multiplier": 4,

        },
        },
        "exits": {
            "south": "(1,2)",
            "east": "(2,3)"
        }
    },
    "(2,3)": {
        "visited": False,
        "loot": [""],
        "exits": {
            "east": "(3,3)",
            "south": "C",
            "west": "(1,3)",
        }
    },
    "(3,3)": {
        "visited": False,
        "loot": ["sword", "shield"],
        "exits": {
            "west": "(2,3)",
        }
    },
    "(1,2)": {
        "visited": False,
        "loot": [],
        "exits": {
            "north": "(1,3)",
            "east": "C",
            "south": "SW",
        }

    },
    "C": {
        "visited": False,
        "loot": [],
        "exits": {
            "north": "(2,3)",
            "west": "(1,2)",
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
            "north": "(1,2)",
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
