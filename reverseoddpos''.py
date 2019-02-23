S=raw_input().split()
N=len(S)
s=0
for i in S:
  if(s<N):
    if(s%2==0):
      S[s]=i[::-1]
      s=s+1
    else:
      s=s+1
print(" ".join(map(str,S)))
