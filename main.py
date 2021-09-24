import math
#choice = "yes"
result = []

def cube_vol (a):
    v = a ** 3
    return v

def tri_vol (a):
    v = (a ** 3 / (6 * math.sqrt(2)))
    return v

def oct_vol (a):
    v = (2*(1+(math.sqrt(2)))*a*a)
    return v

def show_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|         To the world of geometry        |")
    print("|         1. Calculate V of a cube        |")
    print("|         2. Calculate V of a tetrahedron |")
    print("|         3. Calculate V of a octagon     |")
    print("|         4. Exit                         |")
    print("===========================================")


while True:
    show_menu()
    try:
        menu_choice = int(input("Choose 1, 2, 3 or 4 to exit "))
    except ValueError:
        print("--->You cannot choose a float digit<---")
        menu_choice = 0
       
    if menu_choice == 1:
        a = int(input("Enter cm of one side of the cube "))
        volume = cube_vol(a)
        result.append("C")
        result.append(volume)
        print(f"The volume of the cube is: {volume} ");

    elif menu_choice == 2:
        a = int(input("enter cm of the sides of the tetrahedron "))
        volume = tri_vol(a)
        result.append("T")
        result.append(volume)
        print(f"The volume of the tetrahedron is: {volume} ")

    elif menu_choice == 3:
        a = int(input("enter cm of the sides of the octagon "))
        volume = oct_vol(a)
        result.append("O")
        result.append(volume)
        print(f"The volume of the octagon is: {volume} ")

    elif menu_choice == 4:
        seeResult = input("Do you want to see the result? (y/n) ")
        if seeResult == "y":
            print(f"This is the volumes you have calculated: {result}")
            print("Hasta la vista! Thanks for using my program!")
            exit()
        elif seeResult == "n":
            print("Hasta la vista! Thanks for using my program!")
            exit()
        else:
            print("--->Incorrect choice, have another go<---")
    else:
        print("-->Incorrect choice, please try again<--")