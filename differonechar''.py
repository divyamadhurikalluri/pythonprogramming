S=raw_input()
N=len(S)
x=int(N/2)
p=S[0:x]
q=S[x+1:N]
if p==q :
  print("YES")
else:
  print("NO")  
