# Landon added loot to each of the rooms that needed loot
# Tyler fixed the loot bug and added dmg multipliers
room_list = {
    "(1,3)": {
        "visited": False,
        "monster": {
            "type": "Dragon",
            "hp": 300,
            "dmg_multiplier": 1,
        },
        "loot": {
            "type": "Widow Maker",
            "multiplier": 1.5,
            "resistance": 0,
        },
        "exits": {
            "south": "(1,2)",
            "east": "(2,3)"
        }
    },
    "(2,3)": {
        "visited": False,
        "exits": {
            "east": "(3,3)",
            "south": "(2,2)",
            "west": "(1,3)",
        }
    },
    "(3,3)": {
        "visited": False,
        "loot": {
                "type": "A Sharp Sword",
                "multiplier": 1,
                "resistance": 0,
        },
        "exits": {
            "west": "(2,3)",
        }
    },
    "(1,2)": {
        "visited": False,
        "exits": {
            "north": "(1,3)",
            "east": "(2,2)",
            "south": "(1,1)",
        }

    },
    "(2,2)": {
        "visited": False,
        "exits": {
            "north": "(2,3)",
            "west": "(1,2)",
            "south": "(2,1)",
        }
    },
    "(3,2)": {
        "visited": False,
        "exit": True,
        "exits": {
            "south": "(3,1)",
        }
    },
    "(1,1)": {
        "visited": True,
        "exits": {
            "north": "(1,2)",
        }
    },
    "(2,1)": {
        "visited": False,
        "monster": {
            "type": "Skeleton",
            "hp": 100,
            "dmg_multiplier": 1.0,
        },
        "exits": {
            "north": "(2,2)",
            "east": "(3,1)",
        }
    },
    "(3,1)": {
        "visited": False,
        "monster": {
            "type": "Zombie",
            "hp": 100,
            "dmg_multiplier": 1.0,
        },
        "exits": {
            "north": "(3,2)",
            "west": "(2,1)",
        }
    },
}


def set_room_visited(room):
    room_list[room]["visited"] = True
