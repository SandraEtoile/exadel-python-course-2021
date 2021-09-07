import math


def calculate_area_basement_height():
    input_array = input("Enter base and height: ").split(" ")
    height = int(input_array[0])
    base = int(input_array[1])
    return (height * base) / 2


def calculate_area_two_sides_angle():
    input_array = input("Enter two sides and angle between them: ").split(" ")
    a = int(input_array[0])
    b = int(input_array[1])
    angle = int(input_array[2])
    return (a * b * math.sin(math.radians(angle))) / 2


print("Welcome to the triangle area calculation tool")

area_calc_user_choice = 0
menu = '''Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit'''

while area_calc_user_choice <= 3:
    print(menu)
    area_calc_user_choice = int(input("Enter menu item number: "))
    if area_calc_user_choice == 1:
        area = calculate_area_basement_height()
    elif area_calc_user_choice == 2:
        area = calculate_area_two_sides_angle()
    else:
        print('Goodbye!')
        break
    print(f'Area is:  {area:.3f}')
