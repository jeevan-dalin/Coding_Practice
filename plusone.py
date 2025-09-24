#Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.


def plusone(arr):
    num=0
    for i in range(len(arr)):
        if i<len(arr):
            num=num+arr[i]*(10**(len(arr)-i-1))
    newnum=num+1
    print(newnum)
    newstr=str(newnum)
    print(len(newstr))
    newarr=[]
    for i in range(len(newstr)):
        newarrele=newnum//(10**(len(newstr)-i-1))
        newarr.append(newarrele)
        newnum=newnum%(10**(len(newstr)-i-1))
    print(newarr)
    
arr=[]
items=int(input("Enter the number of elements "))
print ("enter the elements now ")
for i in range(items):
    element=int(input())
    arr.append(element)
plusone(arr)