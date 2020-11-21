def number( ):
    i=0
    sum=0
    average=0
    while i<3:
        num=int(input("enter the number"))
        sum=sum+num
        average=sum//3
        i=i+1
    print("nmber of sum",sum)
    print("number of average",average)
number( )