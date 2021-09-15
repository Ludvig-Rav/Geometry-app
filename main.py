import math
print("Hello and welcome, please enter if you need calculation for a cube or a tetrahedron")
shape = input("cube or tetrahedron\n")

if shape == "cube":
    print("Enter cm of one side of the cube")
    a = int(input())
    v = a**3
    print("The volume of the cube is: "); print(v)

if shape == "tetrahedron":
    print("enter cm of the sides of the tetrahedron")
    a = int(input())
    v = (a**3/(6 * math.sqrt(2)))
    print("The volume of the tetrahedron is: "); print(v)