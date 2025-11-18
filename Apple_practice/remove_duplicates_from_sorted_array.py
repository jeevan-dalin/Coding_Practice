# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# The poping solution doesnt cover all the cover cases
# def remove_duplicates(arr):
    
#     for i in range(len(arr)-1):
#         if i==len(arr)-1:
#             return arr
        
#         if arr[i]==arr[i+1]:
#             arr.pop(i+1)
#             if arr[i]==arr[i+1]:
#                 arr.pop(arr[i+1])
#     return arr

# arr=[0,0,1,1,1,1,1,2,2,3,3,4]

# result=remove_duplicates(arr)

# print(arr)

# print(len(arr))

# We will creating a new array from the existing , by comparing the adjacent values

def remove_duplicates(arr):
    newarr=[]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            newarr.append(arr[i])
    newarr.append(arr[len(arr)-1]) # adding the last element , that wont be compared to next , since thats the end
    
    return newarr

arr=[0,0,1,1,1,1,1,1,1,2,2,3,3,4]

result=remove_duplicates(arr)

print(result)

print(len(result))