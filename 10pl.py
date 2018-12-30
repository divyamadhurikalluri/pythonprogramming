s1,s2=raw_input().split(" ")
s = sum([s1[i] != s2[i] for i in range(0,len(s1))])
if s == 1:
    print "yes"
else:
    print "no"
