S,K=input().split()
a=[]
for i in range(0,(len(S)-int(K))+1):
  a.append(S[i:i+int(K)])
print(*a)
