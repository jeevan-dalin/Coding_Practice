# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# def search_insert(arr,num):
#     left=0
#     right=len(arr)-1
#     hashmp={}
#     for i in range(len(arr)):
#         hashmp[arr[i]]=i
    
#     if num in hashmp:
#         return hashmp[num]
#     else:
#         for i in range(len(arr)-1):
#             if num<arr[0]:
#                 return 0
#             elif num>arr[len(arr)-1]:
#                 return len(arr)
#             elif num>arr[i] and num<arr[i+1]:
#                 return i+1
        

# arr=[1,2,3,5]

# num=4

# res=search_insert(arr,num)

# print(res)

#The above solution is not log(n) time complexity. Thus doing the below , its completely using binary search

def search_insert(arr,num):
    left=0
    right=len(arr)-1
    
    while left<=right:
        middle=(left+right)//2
        
        if num> arr[middle]:
            left= middle+1
        elif num<arr[middle]:
            right=middle-1
        else:
            return middle
    
    if arr[middle]<num:
        return middle+1
    else:
        return middle
    
arr=[1,2,3,5]

num=0

res=search_insert(arr,num)

print(res)