S,A=map(str,raw_input().split())
b=[]
if A in S:
  print A
else:
  for i in range(0,len(A)):
    for j in range(0,len(A)):
      if(S[i]==A[j]):
        b.append(S[i])
  print(' '.join(b))       
