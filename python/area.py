"""This code calculate the area of some geometric shapes
 (square,rectangle,triangle,trapezius,diamond,parallelogram,
 circle,sphere and oval)"""
from math import pi


def square():
    side = float(input("Enter side of the square:"))
    print(f"The area of this square: {side ** 2}")


def rectangle():
    length = float(input("Enter length of the rectangle:"))
    width = float(input("Enter width of the rectangle:"))
    print(f"The area of this rectangle: {round((length * width), 2)}")


def triangle():
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    print(f"The area of this triangle:{round((base * height) / 2, 2)}")


def trapezius():
    l_base = float(input("Enter the little base:"))
    b_base = float(input("Enter the big base:"))
    height = float(input("Enter the height:"))
    print(f"The area of this trapezius: {round((l_base + b_base) * (height / 2))}")


def diamond():
    large_diameter = float(input("Enter the large diameter:"))
    small_diameter = float(input("Enter the small diameter:"))
    print(f"The area of this diamond: {round((large_diameter * small_diameter) / 2)}")


def parallelogram():
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    print(f"The area of this parallelogram: {round(base * height, 2)}")


def circle():
    radius = float(input("Enter the radius:"))
    print(f"The area of this circle:{round((radius ** 2) * pi, 2)}")


def sphere():
    radius = float(input("Enter the radius:"))
    print(f"The area of this sphere: {round(4 * (radius**2)* pi, 2)}")


def oval():
    large_diameter = float(input("Enter the large diameter:"))
    small_diameter = float(input("Enter the small diameter:"))
    print(f"The area of this oval: "
          f"{round((large_diameter / 2) * (small_diameter / 2) * pi , 2)}")


li = """
1)Square
2)Rectangle
3)triangle
4)Trapezius
5)Diamond
6)Parallelogram
7)circle
8)sphere
9)oval
"""
print(li)
print("Welcome!!")
while True:
    area_choose = int(input("which area do you want to calculate:"))
    if area_choose == 1:
        square()
    elif area_choose == 2:
        rectangle()
    elif area_choose == 3:
        triangle()
    elif area_choose == 4:
        trapezius()
    elif area_choose == 5:
        diamond()
    elif area_choose == 6:
        parallelogram()
    elif area_choose == 7:
        circle()
    elif area_choose == 8:
        sphere()
    elif area_choose == 9:
        oval()
    else:
        print("Error!!!")
    want = input("Do you want to continue(yes/no):")
    if want.lower() == "no":
        break
    elif want.lower() == "yes":
        pass
    else:
        print("Error!!")
        break
print("Have a nice time:)")
