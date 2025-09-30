#You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.

def remove_duplicates(arr):
    newarr=[]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            newarr.append(arr[i])
    newarr.append(arr[len(arr)-1])
    print(f"List after removing duplicates {newarr} ")

            
arr=[]
items=int(input("Enter the number of array elements"))
print("now enter the elements")
for i in range(items):
    element=int(input())
    arr.append(element)
remove_duplicates(arr)