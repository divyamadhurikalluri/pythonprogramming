S=str(raw_input())
N=len(S)
a=[]
for x in range(0,N,3):
  a.append(S[x])
print(''.join(map(str,a)))
