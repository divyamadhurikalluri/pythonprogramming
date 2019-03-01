S=str(input())
for x in range(1,len(S)):
  P=S[x:]
  if P > S:
    print(P)
    break
