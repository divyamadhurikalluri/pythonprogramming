N,r=int(input()),0
while(N>0):
    d=N%10
    r=r*10+d
    N=N//10
print r
