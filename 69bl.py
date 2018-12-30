N,M=int(input()),int(input())
if N>M:
    l=N-M
    if l%2==0:
        print "even"
    else:
        print "odd"
elif N<M:
    d=M-N
    if d%2==0:
        print "even"
    else:
        print "odd"  
else:
    print "even"         
