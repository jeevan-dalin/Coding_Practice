#You are given a list that contains integers. You need to return the length of the list.

''' Using the lenght function.
def length_of_list(intlist):
    length=len(intlist)
    print(f"The lenght of the list is {length}")

intlist=[]
number_of_items=int(input("Enter the number of list items"))
for i in range(number_of_items):
    element=int(input())
    intlist.append(element)
length_of_list(intlist)

'''


# without using the length fucntion.

def length_of_lists(intlist):
    count=0
    for i in range(len(intlist)):
        count=count+1
    print(f"The total number of items in the list is/are {count}")


intlist=[1,2,3,4,5,6,7,8,9]
length_of_lists(intlist)
        
