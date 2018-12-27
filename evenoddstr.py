S= raw_input()
e,o = [],[]
for i,j in enumerate(S):
    if i % 2 == 0:
        e.append(j)
    else:
        o.append(j)
print ''.join(e), ''.join(o)

