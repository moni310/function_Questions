def calculate(num,num1,ope):
    if ope=="+":
        print(num+num1)
    elif ope=="-":
        print(num-num1)
    elif ope=="*":
        print(num*num1)
    else:
        print(num//num1)
num=int(input("enter the number"))
num1=int(input("enter the number"))
ope=input("enter the number")
calculate(num,num1,ope)