def is_armstrong_number(num):
    # convert the number to a string to find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # calculate the sum of each digit raised to the power of the number of digits
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
        
    # compare the sum to the original number
    return sum == num