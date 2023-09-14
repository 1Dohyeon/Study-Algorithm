n,m=map(int,input().split())
num=list(map(int,input().split()))
result=0

# 모든 경우의 수를 다 계산해야한다.
for i in range(n):
    for j in range(i+1,n):
        for z in range(j+1,n):
            num_sum=num[i]+num[j]+num[z]
            if num_sum<=m:
                result=max(result,num_sum)

print(result)