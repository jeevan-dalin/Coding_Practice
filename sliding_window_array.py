#Problem statement
'''
Given an array of Integers and a window size, calculate the moving average
array = [1,2,3,4,5], w=3 -> moving_avg=[2, 3, 4]
'''
'''
n is size of array , window is 3 .
'''

def sliding_array_avg(array_item):
    try:
        for i in range(len(array_item)):
            sum=0
            if i>=len(array_item)-2:
                break
            else:
                for j in range(i,i+3):
                    if j==len(array_item):
                        break
                    sum=sum+array_item[j]
                avg=sum/3
                array_avg.append(avg)
        print(f"The avg array list is {array_avg}")
    except:
        print("There is issue with logic")

size_of_array=int(input("Enter the size of array "))
array=[]
print("Enter the elements now")
for i in range(0,size_of_array):
    element=int(input())
    array.append(element)
array_avg=[]
sliding_array_avg(array)
