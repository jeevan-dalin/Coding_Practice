# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



def longest_prefix(arr):
    ch=min(arr)
    tmp=''
    j=0
    
    for c in ch:
        for str in arr:
            if c!=str[j]:
                return tmp
        tmp+=c
        j=j+1
    return tmp


list=["flower","flow","flight"]
result=longest_prefix(list)

print(result)


# explanation: from the list find the smallest str, now parse through length of smallest str and list . comparing the char of str to char of strs in list.

