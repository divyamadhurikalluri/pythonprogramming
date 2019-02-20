S=raw_input()
x=int((len(S))/2)
p=S[0:x]
print p
q=S[x+1:len(S)]
print q
if p==q :
  print("YES")
else:
  print("NO")  
