def traverse(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")

arr=[]
number_of_elements=int(input("enter the number of elements"))

for i in range(number_of_elements):
    element=int(input())
    arr.append(element)

print(arr)

print( " after traversing")

traverse(arr)