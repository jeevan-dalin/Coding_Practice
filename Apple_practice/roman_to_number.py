

def roman_to_number(str):
    sum=0
    n=len(str)
    i=0
    hmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    while i<n:
        if i<n-1 and hmap[str[i]]<hmap[str[i+1]]:
            sum+=hmap[str[i+1]]-hmap[str[i]]
            i+=2
        else:
            sum+=hmap[str[i]]
            i+=1
    return sum

str="MCMXCVI"

result=roman_to_number(str)

print(result)