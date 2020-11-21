def number(parameter):
    number1=num
    while number1>=0:
        if number1%2==0:
            print(number1,"even number")
        else:
            print(number1,"odd number")
        number1=number1-1
num=int(input("enter the number"))
number(num)

