def is_armstrong_number(num):
    return sum(int(digit) ** len(str(num)) for digit in str(num)) == num