def add_numbers(number):
    add = 0
    while number > 0:
        digit = number % 10
        add += digit
        number //= 10
    return add