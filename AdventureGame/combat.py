import random
from room_definitions import room_list

damage = 0
critical = 0
num = 0

dmg_multi = 1


def get_user_action():
    return input("Do you want to attack, defend, or heal? ").strip().lower()


# Create function to generate critical and number values
def calc_attack_numbers():
    global damage
    global critical
    global num

    critical = random.randint(1, 7)
    num = random.randint(1, 7)
    if critical == num:
        damage = random.randint(20, 40) * 2 * dmg_multi
    else:
        damage = random.randint(20, 40) * dmg_multi


# Create function to check if critical hit
def is_critical():
    return critical == num


# Monster attack
def monster_attack(hp, current_room):
    calc_attack_numbers()

    monster_multiplier = room_list[current_room]["monster"]["dmg_multiplier"]
    monster_damage = damage * monster_multiplier
    print("The monster attacks you and deals " + str(monster_damage) + " damage to you!")
    return hp - monster_damage


def combat_round(mh, hp, attack, defend, heal, current_room):
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
        hp = monster_attack(hp, current_room)

    return {"hp": hp, "mh": mh}


#Landon did the loot Function
def loot(current_room):
    global dmg_multi
    weapon = room_list[current_room]["loot"]
    loot_decision = input("You see a shiny box in the room do you want to open it, you will never get a second chance.")
    if loot_decision == "yes":
        print("You found " + weapon["type"] + "!")
        multiplier = weapon["multiplier"]
        dmg_multi = dmg_multi + multiplier
    elif loot_decision != "no":
        loot(current_room)

f