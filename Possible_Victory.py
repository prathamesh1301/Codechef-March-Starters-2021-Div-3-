r,o,c=list(map(int,input().split()))
diff=r-c
overRemain=20-o
maxxInRemain=overRemain*6*6
if(maxxInRemain>diff):
    print("YES")
else:
    print("NO")
