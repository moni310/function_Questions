def multiple(list,list1):
    i=0
    empty_list=[ ]
    while i<len(list):
        m=list[i]*list1[i]
        empty_list.append(m)
        i=i+1
    print(empty_list)
multiple([6,8,4,3],[6,3,1,7])
    
  