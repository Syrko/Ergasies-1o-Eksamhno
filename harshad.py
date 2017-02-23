for i in range(1,1001):
    temp=i
    s1=0
    s2=1
    while(temp!=0):
        s1+=+temp%10
        s2*=(temp%10)
        temp=temp/10
    if(i%s1==0):
        print "O %d einai arithmos Harshad" %(i)
    if(s2!=0 and i%s2==0):
        print "O arithmos %d diaireitai apo to ginomeno twn pshfiwn tou" %(i)
