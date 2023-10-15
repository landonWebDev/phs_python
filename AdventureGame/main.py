from room_definitions import room_list, set_room_visited
from combat import combat_round
from movement import move_player, move_north, move_east, move_west, move_south

# Set health variables
mh = 0
hp = 120

# Set constant values
attack = "attack"
defend = "defend"
heal = "heal"
current_room = "SW"


# Resolve winner now that combat is over
def winner():
    if mh <= 0:
        print("You killed the monster, keep exploring to find the way out!")
    elif hp <= 0:
        print("You died")


print("You wake up in a mysterious room, you must find your way out, but be careful because there are monsters in "
      "some of these rooms as well! I wish you the best of luck!")
# while loop to check if you or monster are dead
# Do combat if no winner yet


while "exit" not in room_list[current_room]:
    original_current = current_room
    direction = move_player(current_room)
    if direction == "north":
        current_room = move_north(current_room)
    elif direction == "east":
        current_room = move_east(current_room)
    elif direction == "south":
        current_room = move_south(current_room)
    elif direction == "west":
        current_room = move_west(current_room)

    # check if monster in room if so do combat
    if not room_list[current_room]["visited"]:
        # handle conditional statements from new room
        set_room_visited(current_room)

        if current_room in room_list and "monster" in room_list[current_room]:
            monster = room_list[current_room]["monster"]
            print("Alert! There is a " + monster["type"] + " in this room")
            mh = monster["hp"]
            while mh > 0:
                if mh <= 0:
                    mh = 0
                elif hp <= 0:
                    break
                results = combat_round(mh, hp, attack, defend, heal, current_room)
                hp = results["hp"]
                mh = results["mh"]
            #     update values from results of combat
            winner()

        if hp <= 0:
            break
        else:
            print("There is no monster in this room")
    else:
        if original_current == current_room:
            print("You hit a wall")
        else:
            # If new room equals old room, you hit a wall
            print("You recognize this room and there is nothing new in here")


# end game with winning or losing print
if hp > 0:
    print("Congratulations, you beat the game!")
else:
    print("Try again")
