# Landon added loot to each of the rooms that needed loot
# Tyler fixed the loot bug and added dmg multipliers
# Samuel Added 4 more rooms to the game and made another piece of loot
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
    "(4,3)": {
        "visited": False,
        "monster": {
                "type": "Golem",
                "hp": 600,
                "dmg_multiplier": 2,
                },
        "loot": {
            "type": "Golem Fist",
            "multiplier": 1,
        },
        "exits": {
            "east": "(5,3)",
            "south": "(4,2)",
        },
    },
    "(5,3)": {
        "visited": False,
        "exit": True,
        "exits": {
            "east": "(6,3)",
            "south": "(5,2)",
            "west": "(4,3)",
        },
    },
    "(6,3)": {
        "visited": False,
        "exits": {
            "west": "(5,3)",
        },
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
        "exits": {
            "south": "(3,1)",
            "east": "(4,2)",
        }
    },
    "(4,2)": {
      "visited": False,
      "exits": {
          "north": "(4,3)",
          "east": "(5,2)",
          "west": "(3,2)",

      },
    },
    "(5,2)": {
        "visited": False,
        "exits": {
            "north": "(5,3)",
            "east": "(6,2)",
            "south": "(5,1)",
            "west": "(4,2)",
        },
    },
    "(6,2)": {
        "visited": False,
        "exits": {
            "south": "(6,1)",
            "west": "(5,2)",
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
    "(4,1)": {
        "visited": False,
        "loot": {
            "type": "Strength Ring",
            "multiplier": 1,
            "resistance": 0,
        },
        "exits": {
            "east": "(5,1)",
        }
    },
    "(5,1)": {
        "visited": False,
        "exits": {
            "north": "(5,2)",
            "west": "(4,1)",
            "east": "(6,1)",
        }

    },
    "(6,1)": {
        "visited": False,
        "exits": {
            "north": "(6,2)",
            "west": "(5,1)",
        },
    },

}


def set_room_visited(room):
    room_list[room]["visited"] = True
