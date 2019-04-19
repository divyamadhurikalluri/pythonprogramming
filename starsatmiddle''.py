S=raw_input()
a=len(S)
if(a%2==0):
  k=len(S)//2
  print(S[:k-1]+'*'+'*'+S[k+1:])
else:
  k=len(S)//2
  print(S[:k]+'*'+S[k+1:])

