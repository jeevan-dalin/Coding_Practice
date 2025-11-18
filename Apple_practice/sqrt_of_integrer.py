# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# def sqrt(num):
#     for i in range(num):
#         if i*i==num:
#             return i
        
#         if i*i>num:
#             return i-1
        
# num=4

# res=sqrt(num)

# print(res)

#the above solution is brute force, below one is binary search, which is efficient

def sqrt(num):
    left,right=0,num
    while left<=right:
        middle=(left+right)//2
        if middle**2>num:
            right=middle-1
        elif middle**2<num:
            left=middle+1
            res=middle
        else:
            return middle
    return res

num=15

res=sqrt(num)

print(res)