# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# This is a three pointer problem . X, Y, Z . X is for tracking len of n1 array , y is for n2 array and Z is tracking the whole length.

def merge_soretd_array(arr1,m,arr2,n):
    x=m-1
    y=n-1
    z=m+n-1
# z is starting from the last index of the arr1 and decrements by 1 . The -1 , -1 tells us the range is from 5 till 0 ( becuase -1 is not included ) , the other -1 is for decrement
    for z in range(len(arr1)-1,-1,-1): 
        if x<0: 
            arr1[z]=arr2[y]
            y=y-1
        elif y<0:
            break
        elif arr1[x]<arr2[y]:
            arr1[z]=arr2[y]
            y=y-1
        else:
            arr1[z]=arr1[x]
            x=x-1
    print(arr1)

arr1=[1,2,3,0,0,0]
arr2=[2,5,6]
m=3
n=3

merge_soretd_array(arr1,m,arr2,n)