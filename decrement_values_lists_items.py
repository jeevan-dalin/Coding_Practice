#You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

def decrement_items_value(intlist,decrement_value):
    for i in range(len(intlist)):
        intlist[i]=intlist[i]-decrement_value
    print(f"The list after decrementing {intlist}")

intlist=[]

no_list_elements=int(input("Enter the no of list elements"))

for i in range(no_list_elements):
    element=int(input())
    intlist.append(element)

print(f"The list before decrementing {intlist}")

decrement_items_value(intlist,1)