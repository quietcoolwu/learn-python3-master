def average(*args):
    s=0.0
    if len(args)==0:
        return s
    for x in args:
        s=s+x
    return s/len(args) 



print (average())
print (average(1, 2))
print (average(1, 2, 2, 3, 4))
