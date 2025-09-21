import os, random
import Drawings

# Booleans-------
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
# --------------


# Stats -----------
HP = 50
ATK = 5
health_pot = 1
mana_pot = 1
gold = 0
x = 0
y = 0
HPMAX = 50
stat_num = 10
# Iterate if you add more stats. Used to error check
# ---------------

# Map ---------------------------------
game_map = [['hill', 'river', 'plains', 'cave', 'town', 'vally'],
       ['dungeon', 'vally', 'hill', 'river', 'town', 'cave'],
       ['cave', 'plains', 'hill', 'town', 'river', 'dungeon'],
       ['vally', 'town', 'river', 'hill', 'plains', 'cave'],
       ['river', 'hill', 'dungeon', 'plains', 'vally', 'town'],
       ['town', 'cave', 'plains', 'river', 'hill', 'dungeon']]

biom = {
    "plains" : {
        "t" : "PLAINS",
        "e" : True
    },

    "river" : {
        "t": "RIVER",
        "e": False
    },

    "hill" : {
        "t": "HILL",
        "e": False
    },

    "cave": {
        "t": "CAVE",
        "e": True
    },

    "town": {
        "t": "TOWN",
        "e": False
    },

    "vally": {
        "t": "VALLEY",
        "e": False
    },

    "dungeon": {
        "t": "DUNGEON",
        "e": True
    }
}

current_tile = game_map[y][x]
print(current_tile)
name_of_tile = biom[current_tile]["t"]
print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
print(enemy_tile)


y_len = len(game_map) - 1
x_len = len(game_map[0]) - 1
# Map Info --------------------

# OPPS!!!

opp_list = ["Slime", "Goblin", "Skeleton"]

opps = {
    "Slime":
        {
            "HP" : 10,
            "ATK" : 3,
            "GOLD": 3
        },
    "Goblin":
        {
            "HP": 8,
            "ATK": 5,
            "GOLD": 4
        },
    "DEMON LORD DAN":
        {
            "HP": 100,
            "ATK": 10,
            "GOLD": 1000
        },

    "Skeleton":
        {
            "HP": 10,
            "ATK": 5,
            "GOLD": 8
        },

    "ORC":
        {
            "HP": 16,
            "ATK": 8,
            "GOLD": 30
        },

    "DRAGON":
        {
            "HP": 60,
            "ATK": 8,
            "GOLD": 100
        }

}


# Clear --------
def clear():
    os.system("clear")
#-----------------


# Save ----------------------
def save():
    stats = [
        name,
        str(HP),
        str(HPMAX),
        str(ATK),
        str(health_pot),
        str(mana_pot),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")

    for item in stats:
        f.write(item + "\n")
    f.close()
# -----------------------------

# Gameplay Functions
def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX

    print(f"{name} has gained {amount} HP!")

def battle():

    global fight, play, run, HP, health_pot, mana_pot, gold

    enemy = random.choice(opp_list)
    enemy_hp = opps[enemy]["HP"]
    enemy_MAXHP = enemy_hp
    enemy_atk = opps[enemy]["ATK"]
    enemy_gold = opps[enemy]["GOLD"]

    while fight:
        clear()
        Drawings.draw_line()
        print(f"Defeat the {enemy}!")
        Drawings.draw_line()
        print(f"{enemy}'s HP: {enemy_hp}/{enemy_MAXHP}")
        print(f"{name}'s HP: {HP}/{HPMAX}")
        print(f"{name}'s Health Potions: {health_pot}")
        print(f"{name}'s Mana Potions: {mana_pot}")
        Drawings.draw_line()
        print("1 - Attack")
        if health_pot > 0:
            print("2 - Use Health Potion")
        elif mana_pot > 0:
            print("3 - Use Mana Potion")
        Drawings.draw_line()

        choice = int(input("# "))

        if choice == 1:
            enemy_hp -= ATK
            print(f"{name} did {ATK} damage to {enemy}.")
            if enemy_hp > 0:
                HP -= enemy_atk
                print(f"{enemy} did {enemy_atk} damage to {name}")
                input("> ")

        elif choice == 2:
            if health_pot > 0:
                health_pot -= 1
                heal(30)
                HP - enemy_atk
                print(f"{enemy} did {enemy_atk} damage to {name}")
                input("> ")
            else:
                print("You have no potions!")

        elif choice == 3:
            if mana_pot > 0:
                mana_pot -= 1
                heal(50)
                HP - enemy_atk
                print(f"{enemy} did {enemy_atk} damage to {name}")
                input("> ")
            else:
                print("You have no potions!")

        if HP <= 0:
            print(f"{enemy} defeated {name}")
            fight = False
            run = False
            play = False
            print("GAME OVER")
            input("> ")
            quit()

        if enemy_hp < 0:
            print(f"{name} defeated {enemy}")
            fight = False

            # Drop Rewards!!
            gold += enemy_gold
            if random.randint(0, 100) < 30:
                health_pot += 1
                print("You found a health potion!")

            if random.randint(0, 100) < 10:
                mana_pot += 1
                print("You found a mana potion!")


# Gameplay Loop ----------
while run:
    while menu:
        # Menu Options ----------
        clear()
        Drawings.draw_dragon()
        Drawings.draw_line()
        print("1. New Game")
        print("2. Load Game")
        print("3. RULES")
        print("4. QUIT GAME")
        Drawings.draw_line()
        # ----------------------

        # Rules ---------------
        if rules:
            print("Here are the rules: ")
            rules = False
            choice = ""
            input("> ")
        choice = input("# ")
        # ----------------------

        # Menu Choices ----------------
        if choice == "1":
            clear()
            Drawings.draw_warrior()
            Drawings.draw_line()
            name = input("What is your name, Adventurer? ")
            menu = False
            play = True

        elif choice == "2":
            try:
                clear()
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == stat_num:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    HPMAX = int(load_list[2][:-1])
                    ATK = int(load_list[3][:-1])
                    health_pot = int(load_list[4][:-1])
                    mana_pot = int(load_list[5][:-1])
                    gold = int(load_list[6][:-1])
                    x = int(load_list[7][:-1])
                    y = int(load_list[8][:-1])
                    key = bool(load_list[9][:-1])
                    print(f"Welcome back \"{name}\"")
                    input("> ")
                    menu = False
                    play = True
            except OSError:
                print("No Save File")
                input("> ")
        elif choice == "3":
            rules = True


        elif choice == "4":
            quit()

        # ------------------------------

    while play:
        save() # Auto Save
        clear()

        # Combat Encounter!!! ----------
        if not standing:
            if biom[game_map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    clear()
                    battle()

        # ---------------------


        Drawings.draw_line()
        print(f"Location: " + biom[game_map[y][x]]["t"])
        Drawings.draw_line()
        print(f"Name: {name}")
        print(f"HP: {HP}/{HPMAX}")
        print(f"ATK: {ATK}")
        print(f"Health Pots: {health_pot}")
        print(f"Mana Pots: {mana_pot}")
        print(f"Gold: {gold}")
        print(f"CORD: {y}{x}")
        Drawings.draw_line()
        print("0 - SAVE AND QUIT")
        print("1 - NORTH")
        print("2 - EAST")
        print("3 - SOUTH")
        print("4 - WEST")
        print("5 - Drink Health Potion")
        print("6 - Drink Mana Potion")
        Drawings.draw_line()
        dest = input("# ")

        # Gameplay Options!
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -= 1
                standing = False
            else:
                y = y_len
                standing = False
        elif dest == "2":
            if x < x_len:
                x += 1
                standing = False
            else:
                x = 0
                standing = False
        elif dest == "3":
            if y < y_len:
                y += 1
                standing = False
            else:
                y = 0
                standing = False
        elif dest == "4":
            if x > 0:
                x -= 1
                standing = False
            else:
                x = x_len
                standing = False
        elif dest == "5":
            if health_pot > 0:
                health_pot -= 1
                heal(30)
                print(f"{name} gained 30 HP!")
                input("> ")
            else:
                print("You have no potions!")
            input("> ")
            standing = True
        elif dest == "6":
            if mana_pot > 0:
                mana_pot -= 1
                heal(50)
                print(f"{name} gained 30 HP!")
                input("> ")
            else:
                print("You have no potions!")

            input("> ")
            standing = True

# -------------------