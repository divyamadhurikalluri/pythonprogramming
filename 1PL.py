S = raw_input()
r = []
l = len(S)
for i in xrange(l,0,-1):
    r.append( S[ i - 1] )
print "".join(r)

