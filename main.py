import math
print("Hello and welcome")
choice = "yes"
while choice == "yes":
    print("please enter if you need calculation for a cube or a tetrahedron")
    shape = input("c for cube or t for tetrahedron\n")

    if shape == "c":
        print("Enter cm of one side of the cube")
        a = int(input())
        v = a ** 3
        print("The volume of the cube is: ");
        print(v)
        print("Do you want to go again? yes or no. ")
        choice = input("")

    if shape == "t":
        print("enter cm of the sides of the tetrahedron")
        a = int(input())
        v = (a ** 3 / (6 * math.sqrt(2)))
        print("The volume of the tetrahedron is: ");
        print(v)
        print("Do you want to go again? yes or no. ")
        choice = input("")