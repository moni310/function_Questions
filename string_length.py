def string_function(name,name1):
    if len(name)>len(name1):
        print(name,"name length is more than name1")
    elif len(name)<len(name1):
        print(name1,"name1 length is more than name")
    else:
        print("name1 and name is equal")
name=input("enter the any alpha")
name1=input("enter the any alpha")
string_function(name,name1)


