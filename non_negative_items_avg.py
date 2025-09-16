#You are given a list arr that contains integers. You need to return average of the non negative integers.


def non_negative_avg(arr):
    sum=0
    avg=0
    for i in range(len(arr)):
        if arr[i]>=0:
            non_negative_arr.append(arr[i])
    
    for i in range(len(non_negative_arr)):
        sum=sum+non_negative_arr[i]
    avg=sum/len(non_negative_arr)
    print(f"The avg of non negative items of the list is {avg}")
    
non_negative_arr=[]
arr=[]
no_of_items=int(input("Enter the no of items in lists "))
print("Now enter the list elements ")
for i in range(no_of_items):
    element=int(input())
    arr.append(element)

non_negative_avg(arr)