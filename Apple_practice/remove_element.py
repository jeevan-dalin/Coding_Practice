# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# def remove_element(num,arr):
#     res=[]
#     for i in range(len(arr)):
#         if arr[i]!=num:
#             res.append(arr[i])
            
#     print(res)
    
#     print(len(res))
    
# num=2
# arr=[0,1,2,2,3,0,4,2]

# remove_element(num,arr)


#The above solution isnt efficient even though its O(n) , but the space complexity is not S(1)

#the below is more efficient

def remove_element(arr,num):
    i=0
    j=len(arr)
    
    while i<=j:
        if arr[i]==num:
            arr[i]=arr[j-1]
            j-=1
        else:
            i+=1
    print(arr)
    print(j)

num=2
arr=[2,3,3,2]

remove_element(arr,num)