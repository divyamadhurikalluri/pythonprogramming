S=raw_input()
N=len(S)
for i in range(0,N):
  p=S[:i]+S[i+1:]
  if (p[:]==p[::-1]):
    print("YES")
    break
else:
  print("NO")  
