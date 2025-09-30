#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twosum(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                print(i,j)

arr=[]

items=int(input("Enter the number of items in the list"))

print("Enter the elements now")

for i in range(items):
    element=int(input())
    arr.append(element)

print("Enter the target integer")
k=int(input())

print(f"The input list is {arr}")
twosum(arr,k)