# Switch to the directory where you want the project to live.
# For instance, if it is in C:/lgutz/projects/development
# Open a terminal and type in (no quotes):
#   cd C:/lgutz/projects/development
# Once in that directory, copy and paste the next line:
# git clone https://github.com/landonWebDev/phs_python.git
# This will copy all of your files from your repository down to your
# computer.
# Open an existing project in pycharm to the "phs_python"

import random
import time
from room_definitions import room_list, move_north, move_east, move_west, move_south, set_room_visited

damage = 0
critical = 0
num = 0

# Set health variables
mh = 0
hp = 120

# Set constant values
attack = "attack"
defend = "defend"
heal = "heal"
current_room = "SW"


def movement():
    doors = ', '.join(list(room_list[current_room]["exits"]))
    # print('In Movement, current room is:', current_room)
    move = input("You see doors to the " + doors + ". Which way do you want to go? ").strip().lower()
    if move != "north" and move != "south" and move != "east" and move != "west":
        movement()
    return move


# Create function to generate critical and number values
def calc_attack_numbers():
    global damage
    global critical
    global num

    critical = random.randint(1, 7)
    num = random.randint(1, 7)
    if critical == num:
        damage = random.randint(20, 40) * 2
    else:
        damage = random.randint(20, 40)


# Create function to check if critical hit
def is_critical():
    return critical == num


# Monster attack
def monster_attack():
    calc_attack_numbers()
    global hp
    monster_multiplier = room_list[current_room]["monster"]["dmg_multiplier"]
    monster_damage = damage * monster_multiplier
    print("The monster attacks you and deals " + str(monster_damage) + " damage to you!")
    hp = hp - monster_damage


def get_user_action():
    return input("Do you want to attack, defend, or heal? ").strip().lower()


def combat():
    global mh
    global hp
    global attack
    global defend
    global heal

    # Print out something about beginning combat and current health amounts

    # First thing in combat is to update numbers for attack and critical
    print("You are at " + str(hp) + " health and the monster has " + str(mh) + " health left!")
    calc_attack_numbers()

    # User input for action
    action = get_user_action()
    while action != attack and action != defend and action != heal:
        print("Invalid action, try again.")
        action = get_user_action()

    # Conditionals for actions
    # Attack
    if action == attack:
        if is_critical():
            print("Critical Hit")
        print("You attack the monster and deal " + str(damage) + " damage to the monster!")
        mh = mh - damage
    # Defend
    elif action == "defend":
        print("You defend yourself and take no damage this turn!")
    # Heal
    elif action == "heal":
        print("You heal yourself and gain 50 hp!")
        hp += 50
    if action != defend and mh > 0:
        monster_attack()


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
    direction = movement()
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
                combat()
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
