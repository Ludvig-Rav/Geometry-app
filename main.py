import math
print("Hello and welcome")
choice = "yes"

def cube_vol (a):
    v = a ** 3
    return v

def tri_vol (a):
    v = (a ** 3 / (6 * math.sqrt(2)))
    return v

def oct_vol (a):
    v = (2*(1+(math.sqrt(2)))*a*a)
    return v

while choice == "yes":
    print("please enter if you need calculation for a cube, a tetrahedron or a octagon")
    shape = input("c for cube, t for tetrahedron and o for octagon\n")

    if shape == "c":
        print("Enter cm of one side of the cube")
        a = int(input())
        volume = cube_vol(a)
        print(f"The volume of the cube is: {volume} ");
        print("Do you want to go again? yes or no. ")
        choice = input("")

    if shape == "t":
        print("enter cm of the sides of the tetrahedron")
        a = int(input())
        volume = tri_vol(a)
        print(f"The volume of the tetrahedron is: {volume} ")
        print("Do you want to go again? yes or no. ")
        choice = input("")

    if shape == "o":
        print("enter cm of the sides of the octagon")
        a = int(input())
        volume = oct_vol(a)
        print(f"The volume of the octagon is: {volume} ")
        print("Do you want to go again? yes or no. ")
        choice = input("")

if choice == "no":
    print("Hasta la vista!")
    exit()