#You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.


def seperate_even_odd(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            evenarr.append(arr[i])
        else:
            oddarr.append(arr[i])
    
    print("even :",end=" ")
    for i in range(len(evenarr)):
        print(evenarr[i],end=" ")
    print("odd :",end=" ")
    for i in range(len(oddarr)):
        print(oddarr[i],end=" ")
    
evenarr=[]
oddarr=[]
arr=[]
items_count=int(input("Enter the no of list items "))

print("Now enter the list items ")
for i in range(items_count):
    element=int(input())
    arr.append(element)

print("RUnning the seperation function now ")

seperate_even_odd(arr)