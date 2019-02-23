N,M=map(int,raw_input().split())
A=map(int,raw_input().split())
B=map(int,raw_input().split())
A.sort()
B.sort()
X=' '.join(map(str,A))
Y=' '.join(map(str,B))
if (Y in X):
  print("YES")
else:
  print("NO")  
