import os
import Drawings

# Booleans-------
run = True
menu = True
play = False
rules = False
key = False
# --------------


# Stats -----------
HP = 50
HPMAX = 50
ATK = 5
health_pot = 1
mana_pot = 1
gold = 0
x = 0
y = 0
stat_num = 9 # Iterate if you add more stats. Used to error check
# ---------------

# Map
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
                f = open("load.txt2", "r")
                load_list = f.readlines()
                if len(load_list) == stat_num:
                    name = int(load_list[0][:-1])
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    health_pot = int(load_list[3][:-1])
                    mana_pot = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    print(f"Welcome back \"{name}\"")
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
        Drawings.draw_line()
        dest = input("# ")

        # Loop to Send you Back to the Menu
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -= 1
            else:
                y = y_len
        elif dest == "2":
            if x < x_len:
                x += 1
            else:
                x = 0
        elif dest == "3":
            if y < y_len:
                y += 1
            else:
                y = 0
        elif dest == "4":
            if x > 0:
                x -= 1
            else:
                x = x_len
# -------------------