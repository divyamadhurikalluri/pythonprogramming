N=int(raw_input())
l=list(map(int,raw_input().split()))
b=l[::-1]
print('->'.join(map(str,b)))  
