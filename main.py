import random
import time
from room_definitions import room_list, current_room


damage = 0
critical = 0
num = 0

# Set health variables
mh = 100
hp = 100

move = ""
# Set constant values
attack = "attack"
defend = "defend"
heal = "heal"

print("You wake up in a mysterious room, you must find your way out, but be careful because there are monsters in "
      "some of these rooms as well! I wish you the best of luck!")


def movement():
    global move
    move = input("Do you want to travel north, south, east, or west? ").strip().lower()
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
    monster = room_list[current_room]["monster"]
    multiplier = monster["dmg_multiplier"]
    print("the monster is a ", monster["type"], " and has ", monster["hp"], " health! This monster deals ", monster["dmg_multiplier"], " times damage!")
    monster_damage = damage * multiplier
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
        get_user_action()

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
        print("You heal yourself and gain 40 hp!")
        hp += 40
    if action != defend and mh > 0:
        monster_attack()


# Resolve winner now that combat is over
def winner():
    if mh <= 0:
        print("You killed the monster, good job")
    elif hp <= 0:
        print("You died")


# while loop to check if you or monster are dead
# Do combat if no winner yet
while mh > 0:
    if mh <= 0:
        mh = 0
    elif 0 > hp:
        break

    combat()
winner()
