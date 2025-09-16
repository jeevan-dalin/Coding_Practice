#You are given a list that contains integers. You need to return the sum of the list.

def sum_of_lists(intlist):
    sum=0
    for i in range(len(intlist)):
        sum=sum+intlist[i]
    print(f"The sum of all elements in the lists is {sum}")
    

intlist=[]
no_of_items=int(input("Enter the no of elements in the list"))
for i in range(no_of_items):
    element=int(input())
    intlist.append(element)
    
sum_of_lists(intlist)