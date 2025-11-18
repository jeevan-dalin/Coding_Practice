# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def pascal_triangle(num):
    triarr=[[1]]
    
    if num==1:
        return triarr
    else:
        for i in range(num-1):
            prearr= [0] + triarr[-1] + [0]
            newarr=[]
            for j in range(len(triarr[-1])+1):
                newarr.append(prearr[j]+prearr[j+1])
            triarr.append(newarr)
        return triarr

num=5
resul=pascal_triangle(num)

print(resul)