N=int(input())
n=input().split()
a=[]
for x in n:
    a.append(int(x))
print(max(a)-min(a))
