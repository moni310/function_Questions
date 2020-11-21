def minimum(a):  
    b=list[0]
    i=0
    while i<len(list):
        if list[i]<b:
            b=list[i]
        i=i+1
    return(b)
list=[5,3,1,6,5,4,7,6]
print(minimum(list))   
