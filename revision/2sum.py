#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# def twosum(arr,k):
#     for i in range(len(arr)-1):
#         for j in range(i,len(arr)):
#             if arr[i]+arr[j]==k:
#                 print(i,j)
#                 point=1
#         if point==1:
#             break
        
        
        
# arr=[1,2,3,4,5]

# twosum(arr,5)

def twosum(arr,k):
    # hashmap=dict(enumerate(arr))
    # print(hashmap)
    h={} #declaring the dict/hashmap
    
    for i in range(len(arr)): # making value of lists as key for hashmap and index as value to it
        h[arr[i]]=i     #h[key]=value
    
    for i in range(len(arr)): # searching the index where diff value is present. a[i]+a[j]=k
        y=k-arr[i]
        if y in h and h[y]!=i:
            print(i,h[y])
            break
        
arr=[1,2,3,4,5]

twosum(arr,5)


