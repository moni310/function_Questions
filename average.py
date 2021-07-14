def average( ):
    av=0
    i=1
    sum=0
    while i<=3:
        number=int(input("enter the number"))
        sum=sum+number
        av=sum//3
        i=i+1
    print(av)
average( )