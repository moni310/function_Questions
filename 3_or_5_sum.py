def limit(parameter):
    n=num
    sum=0
    while 0<n:
        number=int(input("enter the number"))
        if number%3==0 or number%5==0:
            sum=sum+number
        n=n-1
    print(sum)
num=int(input("enter the number"))
limit( num)   