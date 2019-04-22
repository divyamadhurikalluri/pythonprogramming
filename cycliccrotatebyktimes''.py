N,K= map(int,raw_input().split())
L= list(map(int,raw_input().split()))
K=K%N
a= L[-K:] + L[:-K]
print(' '.join(map(str,a)))
'''
N,K= map(int,input().split())
L= list(map(int,input().split()))
K=K%N
a= L[-K:] + L[:-K]
print(*a)
'''
