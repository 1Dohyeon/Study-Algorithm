import sys

n=int(sys.stdin.readline())
p=[0]+list(map(int,sys.stdin.readline().split()))   
d=[0]*(n+1) 
d[1]=p[1]  

for i in range(2,n+1):
    for j in range(1, i+1):
        if d[i]==0:
            d[i]=d[i-j]+p[j]
        else:
            d[i]=min(d[i],d[i-j]+p[j])  # 앞 문제와 달리 최댓값이 아니라 최솟값이기 때문에 max대신 min으로 바꿔준다.
print(d[i])                             # 하지만 바꾸기만 하면 d[i]=0이라는 값도 나오므로 d[i]=0일 때 d[i]=d[i-j]+p[j] 
                                        # 를 대입하여 한번도 안사는 경우를 없앤다.
