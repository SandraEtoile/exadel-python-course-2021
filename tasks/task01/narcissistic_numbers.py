def count_digits(number, digits):
    n = number
    number_of_digits = 0
    while n != 0:
        digits.append(n % 10)
        n //= 10
        number_of_digits += 1
    return number_of_digits


def is_narcissistic_number(number):
    digits = []
    number_of_digits = count_digits(number, digits)
    powers = []
    for d in digits:
        power = d**number_of_digits
        powers.append(power)
    return sum(powers) == number


narcissistic_numbers = []

for i in range(1, 1001):
    if is_narcissistic_number(i):
        narcissistic_numbers.append(i)

print(narcissistic_numbers)
