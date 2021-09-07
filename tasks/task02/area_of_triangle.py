import math


def basement_height_area(height, base):
    return (height * base) / 2


def two_sides_angle(a, b, angleC):
    return (a * b * math.sin(math.radians(angleC))) / 2


print("Welcome to the triangle area calculation tool")

area_calc_user_choice = 0

while area_calc_user_choice < 3:
    print("Menu")
    print("1. Calculate triangle area by base and height")
    print("2. Calculate triangle area by 2 sidea and angle between them")
    print("3. Exit")
    area_calc_user_choice = int(input("Enter menu item number: "))
    if area_calc_user_choice == 1:
        input_array = input("Enter base and height: ").split(" ")
        height = int(input_array[0])
        base = int(input_array[1])
        area = basement_height_area(height, base)
        print("Area is: " + str(area))
    elif area_calc_user_choice == 2:
        input_array = input("Enter two sides and angle between them: ").split(" ")
        a = int(input_array[0])
        b = int(input_array[1])
        angle = int(input_array[2])
        area = two_sides_angle(a, b, angle)
        print("Area is: " + str(area))