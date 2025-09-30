#You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

def move_zeroes_to_end(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j=j+1
    print(arr)
    
arr=[]

items=int(input("Enter the number of items for the list"))

print("Now enter the items ")

for i in range(items):
    element=int(input())
    arr.append(element)

move_zeroes_to_end(arr)
            
            