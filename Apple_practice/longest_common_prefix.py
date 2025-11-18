# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longest_common_prefix(list):
    tmp=""
    j=0
    min_length=10000000
    ch=min(list) #using the min is not right , because min is not checking lenght of a string.
    
    for c in ch:
        for i in list:
            if c != i[j]:
                return tmp
        tmp=tmp+c
        j=j+1
    return tmp
    
list=["flower","flow","flight"]

result=longest_common_prefix(list)

print(result)
                