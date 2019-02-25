N=raw_input()
p=0
for x in range(0,len(N)):
    for y in range(0,x+1):
        p=p+int(N[y])
print p
