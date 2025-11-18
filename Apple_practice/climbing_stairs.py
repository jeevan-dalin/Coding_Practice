# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# #  This is DP problem which represnts a fibonacci series , that start from 1,2.

## The below is the program for fibonacci series , which is DP problem that can solved using recursion, memoition and tabulation.
## The below program is printing the series 
# def fibonacci(num):
#     if num<=1:
#         return num
#     return fibonacci(num-2)+fibonacci(num-1)

# num=6
# arr=[]
# for i in range(num):
#     arr.append(fibonacci(i))

# print(arr)

## Recursive soltuion to the problem of climb stairs:

# def climbstairs(n):
#     if n<=3:
#         return n
#     else:
#         return climbstairs(n-2)+climbstairs(n-1)

# n=0

# result=climbstairs(n)

# print(result)


# ## Memoisation // also called top down approach . 

# def climbstairs(n):
#     memo={1:1,2:2,3:3}
    
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n]=climbstairs(n-2)+climbstairs(n-1)
#         return memo[n]
    
# n=3
# result=climbstairs(n)

# print(result)

# Tabulation method // Also called as the Bottm up approach

def climbstairs(n):
    arr=[0]*n
    arr[0]=1
    arr[1]=2
    if n<=2:
        return n
    else:
        for i in range(2,n):
            arr[i]=arr[i-2]+arr[i-1]
        return arr[n-1]
    
n=4

result=climbstairs(n)

print(result)





