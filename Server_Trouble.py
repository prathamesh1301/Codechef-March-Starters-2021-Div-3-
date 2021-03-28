import math
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    if(n%k==0):
        dis=int(n/k)
        pairs=k
    else:
        dis=int(math.floor(n/k))+1
        pairs=n-k*(int(math.floor(n/k)))
    print(dis,pairs)
    
