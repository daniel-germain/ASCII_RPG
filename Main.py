import os
import Drawings

run = True
menu = True
play = False
rules = False

# Stats
HP = 50
ATK = 5

# Clear
def clear():
    os.system("clear")

# ASCII ART-----------
def draw():
    print("X-------------------X")

# Save ----------------------
def save():
    stats = [
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.txt", "w")

    for item in stats:
        f.write(item + "\n")
    f.close()
# -----------------------------

# Gameplay Loop
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
            clear()
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            print(f"Welcome back \"{name}\"")

        elif choice == "3":
            rules = True


        elif choice == "4":
            quit()

        # ------------------------------

    while play:
        save() # Auto Save

        Drawings.draw_line()
        print("0 - SAVE AND QUIT")
        Drawings.draw_line()
        dest = input("# ")

        # Loop to Send you Back to the Menu
        if dest == "0":
            play = False
            menu = True
            save()