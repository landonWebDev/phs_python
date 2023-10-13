room_list = {
    "NW": {
        "monster": {
            "type": "Dragon",
            "hp": 1000,
            "dmg_multiplier": 2,
        },
        "loot": [],
        "exits": {
            "south": "W",
            "east": "N"
        }
    },
    "N": {
        "loot": [],
        "exits": ["south", "east", "west"]
    },
    "NE": {
        "loot": ["sword", "shield"],
        "exits": ["west"]
    },
    "W": {
        "exits": ["north", "east", "south"]

    },
    "C": {
        "exits": ["north", "south", "west"]
    },
    "E": {
        "exits": [" south", "east"]
    },
    "WW": {

    },
    "S": {

    },
    "SE": {

    },
}

current_room = "NW"


def move_north():
    global current_room

    if 'north' in room_list[current_room]["exits"]:
        current_room = room_list[current_room]["exits"]["north"]
        print('new current room: ', current_room)


def move_east():
    global current_room

    if 'east' in room_list[current_room]["exits"]:
        current_room = room_list[current_room]["exits"]["east"]
        print('new current room: ', current_room)


def move_south():
    global current_room

    if 'south' in room_list[current_room]["exits"]:
        current_room = room_list[current_room]["exits"]["south"]
        print('new current room: ', current_room)


def move_west():
    global current_room

    if 'west' in room_list[current_room]["exits"]:
        current_room = room_list[current_room]["exits"]["west"]
        print('new current room: ', current_room)
# move_east()

# Loop over these actions until either you reach the exit or you die

# Prompt to move character
# Move character
# Update global variables for monster
# Handle combat
# Handle loot
