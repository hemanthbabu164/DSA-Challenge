'''
Convert a number A to B with minimum operations. The operations allowed are : 

1) Subtract current value by 1
2) Multiply the value by 2

Print -1 if it is not possible to convert.

'''
# vfovmorvmrv
# 1. View Products
def convert(A, B):
 
    if(A == B):
        return 0

    if(A > B):
        return A - B
 
    if(A <= 0 and B > 0):
        return -1       # not possible
 
    if(B % 2 == 1):
        # doing '-1' on A equivalent to (+1 on B)
        return 1 + convert(A, B + 1)
    else:
        # doing '*2' on A equivalent to  n/2 or n:
        return 1 + convert(A, B / 2)
    
A=int(input("Enter A:"))
B=int(input("Enter B:"))

print("Minimum number of operations = ",convert(A,B))