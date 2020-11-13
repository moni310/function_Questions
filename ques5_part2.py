def check_function( ):
    list1=[2,9,6,7,3,8]
    list2=[8,5,8,10,7,3]
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("both number is even")
        elif list1[i]%2!=0 and list2[i]%2!=0:
            print("both number is odd")
        else:
            print("one is odd and one is even")
        i=i+1
check_function()