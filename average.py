N,l,k = int(input()),0,0
a=[]
for n in range(N):
    a.append(input())
for  m in a:   
    l = l+m;
k = l/N
print(k)
