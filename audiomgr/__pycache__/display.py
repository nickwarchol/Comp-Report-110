import os
def print_menu():
    print("-" * 20)
    print("** Audio Manager **")
    print("-" * 20)

    print("[1] Register a New Album")
    print("[2] Register a New Song")
    print("[3] Display album catalog")
    print("[4] Print the songs inside the new Album")
    print("[5] Count all the songs in the system")
    print("[6] Total $ in the catalag")
    print("[7] Most expensive Album")
    print("[10] Change the title of the specific Album")
    

    print("[q] Quit")

def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)


def clear():
    if(os.name == 'nt' ):
        return os.system("cls")
    else:
        return os.system("clear")

    # this is the same in one line \\
    # return os.system('cls' if os.name == 'nt' else 'clear')