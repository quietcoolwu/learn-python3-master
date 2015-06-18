L = []
for m in range(1,10):
    for n in range(0,10):
        for i in range(0,10):
            if m==i:
                L.append(100*m+10*n+i)   
print (L)        