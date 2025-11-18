# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def validate_string(str):
    tmp=[]
    hashmap={')':'(','}':'{',']':'['}
    for i in str:
        if i in hashmap:
            if not tmp or tmp.pop()!=hashmap[i]: # not tmp meaning - if tmp is empty its considered as false , thus not false is true.
                return False
        else:
            tmp.append(i)
        print(tmp)
    return not tmp

str=''

result=validate_string(str)

print(result)