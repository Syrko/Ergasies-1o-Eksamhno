a=input("Input list in '[x1, x2, ..., xn]' format: ")
ctr=0
for i in range(len(a),0,-1):
    if a[i-1]==0:
        for j in range(i,len(a)-ctr):
            a[j-1], a[j]=a[j], a[j-1]
        ctr+=1
print a
