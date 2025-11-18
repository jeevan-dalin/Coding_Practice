# Given an integer x, return true if x is a palindrome, and false otherwise.

def int_palindrome(num):
    newnum=0
    digit=0
    
    while num>0:
        digit=num%10
        newnum=(newnum*10)+digit
        num=num//10
    return newnum

num=123
reveresed_num=int_palindrome(num)
print(reveresed_num)

if num==reveresed_num:
    print("palindrome")
else:
    print("not palindrome")