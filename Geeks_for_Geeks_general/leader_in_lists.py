#You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

def leader_in_lists(arr):
    high=0
    for i in range(len(arr)):
        max=arr[i]
        for j in range(i,len(arr)):
            if arr[i]>=arr[j]:
                max=arr[i]
            else:
                break
                   
        newarr.append(max)
    print(newarr)
        
arr=[16, 17, 4, 3, 5, 2]
newarr=[]

leader_in_lists(arr)