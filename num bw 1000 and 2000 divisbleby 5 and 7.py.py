n=[]
for x in range (1000,2000):
    if(x%7==0) and (x%5==0):
        n.append(str(x))
print(",".join(n))