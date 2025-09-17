'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

'''

def second_larget(arr):
    flag=0
    arr.sort()
    arrdesc=arr[::-1]
    for i in range(int(len(arrdesc)/2)):
        if arrdesc[i]==arrdesc[len(arrdesc)-1-i]:
            flag=1
    if flag==1:
        print("All values are equal !!!! -1 !!!!")
    else:
        print(f"The second largest element in list is {arrdesc[1]}")

arr=[]

items_count=int(input("Enter the no of elements "))

print("Now enter the elements")

for i in range(items_count):
    element=int(input())
    arr.append(element)

second_larget(arr)