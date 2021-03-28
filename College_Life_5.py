t=int(input())
for i in range(t):
    f,c=list(map(int,input().split()))
    foot=list(map(int,input().split()))
    crick=list(map(int,input().split()))
    current=0    #current=0 for football and 1 for cricket
    i=0
    j=0
    switches=0
    while(i<f and j<c):
        if(current==0):
            if(foot[i]<crick[j]):
                switches+=0
        
                i+=1
                current=0
            else:
                switches+=1
                j+=1
                current=1
        else:
            if(foot[i]>crick[j]):
                switches+=0
                j+=1
                
                current=1
            else:
                switches+=1
                i+=1
                current=0
    if(i<f and current==1):
        switches+=1
       
    if(j<c and current==0):
        switches+=1
       
                
    print(switches)            
            
