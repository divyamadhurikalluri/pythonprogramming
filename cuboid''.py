L,B,H=map(int,raw_input().split())
p=[]
s=2*((L*B)+(B*H)+(H*L))
v=(L*B*H)
p.append(s)
p.append(v)
print(' '.join(map(str,p)))
