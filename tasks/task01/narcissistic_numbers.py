def countDigits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


narcissistic_numbers = []
for i in range(1, 1001):
    number_of_digits = countDigits(i)
    digits = [int(x) for x in str(i)]
    powers = []
    for d in digits:
        power = pow(d, number_of_digits)
        powers.append(power)
    if sum(powers) == i:
        narcissistic_numbers.append(i)
print(narcissistic_numbers)
