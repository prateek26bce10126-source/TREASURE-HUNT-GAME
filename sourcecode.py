import random

# treasure hunt game

places = ["Library", "Laboratory", "Garden", "Cave"]
opt = ("search", "move", "quit")

found_clues = set()

rooms = {
    "Library": {
        "clue": "The next clue is hidden where knowledge is created.",
        "next": "Laboratory"
    },
    "Laboratory": {
        "clue": "You found a mysterious key",
        "next": "Garden"
    },
    "Garden": {
        "clue": "Look for the place surrounded by darkness.",
        "next": "Cave"
    },
    "Cave": {
        "clue": "You found the treasure",
        "next": "Treasure"
    }
}

def instructions():
    print("\n--- INSTRUCTIONS ---")
    print("1. go to locations")
    print("2. look for clues")
    print("3. collect them")
    print("4. make it to the cave")
    print("5. type quit to exit")
    print("-" * 20)

def menu():
    print("\n=== TREASURE HUNT ===")
    print("1. Play")
    print("2. Help")
    print("3. Quit")
    print("=====================")

def play(name):
    loc = "Library"
    found_clues.clear()
    
    print(f"\nWelcome {name} let's start!")
    
    while True:
        print("\nCurrent spot:", loc)
        
        if loc == "Treasure":
            print(f"\nCongrats {name}!!")
            print("you actually found the treasure")
            print("total clues:", len(found_clues))
            break
            
        print("\nWhat do you wanna do?")
        print("1. Search")
        print("2. Move")
        print("3. Quit")
        
        c = input("> ")
        
        if c == "1":
            clue = rooms[loc]["clue"]
            print("\nSearching...")
            print("Got clue:", clue)
            found_clues.add(clue)
            
        elif c == "2":
            next_room = rooms[loc]["next"]
            r = random.randint(1, 3)
            
            if r == 1:
                print("\noh cool, found a shortcut")
            elif r == 2:
                print("\npath looks clear")
            else:
                print("\nweird stuff happened...")
                
            loc = next_room
            print("Moved to:", loc)
            
        elif c == "3":
            print("\nbye bye")
            break
        else:
            print("\ninvalid input, try again")

# main loop
username = input("Enter your name: ")

while True:
    menu()
    m = input("Choice: ")
    
    if m == "1":
        play(username)
    elif m == "2":
        instructions()
    elif m == "3":
        print("see ya!", username)
        break
    else:
        print("huh? wrong choice")