#You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k.


def items_less_than_k(arr,k):
    for val in range(len(arr)):
        if arr[val]<k:
            less_than_arr.append(arr[val])
    print(less_than_arr)
            
less_than_arr=[]
arr=[]
no_of_items=int(input("Enter the number of lists items "))

print("Enter the items now ")

for i in range(no_of_items):
    element=int(input())
    arr.append(element)
    
k=int(input("Now enter the k value "))

items_less_than_k(arr,k)