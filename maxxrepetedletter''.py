S=raw_input()
a=[]
for i in range (0,len(S)):
    a.append(S.count(S[i]))
b=a.index(max(a))
print(S[b])
