def num( ):
    a=1
    count=0
    while a<=number:
        if number%a==0:
            count=count+1
        a=a+1
    if count==2:
        print("it is prime number")
    else:
        print("it is not prime number")
number=int(input("enter the number"))
num( )