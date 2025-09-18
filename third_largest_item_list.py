#Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.

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
        print(f"The third largest element in list is {arrdesc[2]}")

arr=[]

items_count=int(input("Enter the no of elements "))

print("Now enter the elements")

for i in range(items_count):
    element=int(input())
    arr.append(element)

second_larget(arr)