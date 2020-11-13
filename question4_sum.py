def add_numbers(list1,list2):
    i=0
    empty=[ ]
    while i<len(list2):
        sum=list1[i]+list2[i]
        i=i+1
        empty.append(sum)
    print(empty)
list1=[1,4,5,6,2]
list2=[4,7,8,5,9]
add_numbers(list1,list2)