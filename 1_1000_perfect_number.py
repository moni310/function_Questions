def number( ):
    j=1
    while j<1000:
        i=1
        sum=0
        while i<j:
            if j%i==0:
                sum=sum+i
            i=i+1
        if j==sum:
            print(sum,"perfect number")
        j=j+1
number( )