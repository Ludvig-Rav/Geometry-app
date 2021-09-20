import math
print("Hello and welcome")
choice = "yes"

def cube_vol (a):
    v = a ** 3
    return v

def tri_vol (a):
    v = (a ** 3 / (6 * math.sqrt(2)))
    return v

while choice == "yes":
    print("please enter if you need calculation for a cube or a tetrahedron")
    shape = input("c for cube or t for tetrahedron\n")

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