t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ans=len(list(set(a)))
    if(ans<m):
        print("YES")
    else:
        print("NO")
