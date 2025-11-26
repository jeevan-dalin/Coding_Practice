#Revision of two sum problem for the date - 26th Nov.

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# def two_sum(arr,k):
#     for i in range(len(arr)-1):
#         if arr[i]+arr[i+1]==k:
#             print(i,i+1)
            
            
            
# arr=[1,2,3,4,5]

# k=6

# two_sum(arr,k)

#the program isnt efficient , becuase it checks for the consequrnt elements for sum , but what if the elements are consiquent,
# for 6 we need 1+5 , which is 0th element and last element. 

 
# def two_sum(arr,k):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i]+arr[j]==k:
#                 print(i,j)
#                 flag=1 # adding flag to mark the execution of first occurance.
#         if flag == 1:
#             break

# arr=[1,2,3,4,5]

# k=6

# two_sum(arr,k)

# the above solves the problem , but the complexity is O (n^2)

def two_sum(arr,k):
    hmap={}

    for i in range(len(arr)):
        hmap[arr[i]]=i
    
    for i in range(len(arr)):
        target=k-arr[i]
        if target in hmap and hmap[target]!=i:
            print(i,hmap[k-arr[i]])
            break

arr=[3,2,2,3]
k=6
two_sum(arr,k)


# the above solution is optmized one , which uses linear call - O(n).