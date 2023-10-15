from room_definitions import room_list


def move_player(current_room):
    doors = ', '.join(list(room_list[current_room]["exits"]))
    # print('In Movement, current room is:', current_room)
    move = input("You see doors to the " + doors + ". Which way do you want to go? ").strip().lower()
    if move != "north" and move != "south" and move != "east" and move != "west":
        move_player(current_room)
    return move


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
