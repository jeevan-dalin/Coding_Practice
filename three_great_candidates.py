#The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates.

def three_great_candidates(arr):
    arr.sort()
    arrdesc=arr[::-1]
    great_candidate=arrdesc[0]*arrdesc[1]*arrdesc[2]
    return great_candidate

arr=[]
items=int(input("Enter the no of items for the list "))

print("Now enter the items")

for i in range(items):
    element=int(input())
    arr.append(element)

candidate=three_great_candidates(arr)

print(f"The combination of great candidate is {candidate}")