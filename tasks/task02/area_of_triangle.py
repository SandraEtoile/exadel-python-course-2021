import math


def calculate_area_basement_height_user_input():
    user_input = input("Enter base and height: ")
    return calculate(user_input, 2, calculate_area_basement_height, calculate_area_basement_height_user_input)


def calculate_area_basement_height(input_array):
    height = int(input_array[0])
    base = int(input_array[1])
    return (height * base) / 2


def calculate_area_two_sides_angle_user_input():
    user_input = input("Enter two sides and angle between them: ")
    return calculate(user_input, 3, calculate_area_two_sides_angle, calculate_area_two_sides_angle_user_input)


def calculate_area_two_sides_angle(input_array):
    a = int(input_array[0])
    b = int(input_array[1])
    angle = int(input_array[2])
    return (a * b * math.sin(math.radians(angle))) / 2


def calculate(input_values, input_length, area_cal_func, print_area_prompt):
    input_array = input_values.split(" ")
    if len(input_array) != input_length:
        print(f'Please supply {input_length} values')
        return print_area_prompt()
    else:
        for i in input_array:
            if int(i) <= 0:
                print('Please supply non negative and non zero values only')
                return print_area_prompt()
        return area_cal_func(input_array)


print("Welcome to the triangle area calculation tool")

area_calc_user_choice = 0
menu = '''Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit'''

while area_calc_user_choice != 3:
    print(menu)
    area_calc_user_choice = int(input("Enter menu item number: "))
    if area_calc_user_choice == 1:
        area = calculate_area_basement_height()
    elif area_calc_user_choice == 2:
        area = calculate_area_two_sides_angle()
    elif area_calc_user_choice == 3:
        print('Goodbye!')
        break
    else:
        print('Choose the correct value')
    print(f'Area is:  {area:.3f}')
