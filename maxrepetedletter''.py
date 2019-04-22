S=raw_input()
a=[]
for i in range (0,len(s)):
    a.append(S.count(s[i]))
b=a.index(max(a))
print(S[b])
