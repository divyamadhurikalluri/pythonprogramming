N=int(raw_input())
for i in range(N):
  if 2**i==N:
    k=i
    break
print(2**(k+1))

