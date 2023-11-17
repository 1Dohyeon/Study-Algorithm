import sys

n,k=map(int,sys.stdin.readline().split())
mod=1000000000
d=[[0 for i in range(n+1)] for j in range(k+1)]
d[0][0]=1

# d[k][n] 0부터 n까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수 
# x+x+x+x+ ... +x+l=n 이라고 가정한다.
# l은 합분해 식의 마지막 원소이고 l을 제외한 앞에 x들은 k-1개일 것이다.
# 즉 앞에 식들의 합은 n-l이되고 이것을 위 d[k][n]처럼 나타낸다면 d[k-1][n-l]이 된다.
# 따라서 d[k][n]=d[k-1][n-l]의 합 

for i in range(1,k+1):
    for j in range(n+1):
        for l in range(j+1):
            d[i][j]+=d[i-1][j-l]    # 경우의 수이기 때문에 변수 l에 따라 나오는 새로운 경우의 수를 계속 더해줘야한다.
            
print(d[k][n]%mod)

