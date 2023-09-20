# Find LCM of two numbers using GCD

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm_using_gcd(a, b):

    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    
    return lcm


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm_using_gcd(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")


'''
Time complexity : O(log(min(a,b)))
Space complexity : O(log(min(a,b)))

'''
