def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = 0
    for digit_char in num_str:
        digit = int(digit_char)
        armstrong_sum += digit ** num_digits
    return armstrong_sum == num

num1 = 153
print(is_armstrong_number(num1))  # Output: True (153 is an Armstrong number)

num3 = 123
print(is_armstrong_number(num3))  # Output: False (123 is not an Armstrong number)
