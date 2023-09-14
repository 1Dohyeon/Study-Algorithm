import sys

n=int(sys.stdin.readline())
d=[]

for i in range(n):
    d.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(len(d[i])):
        # 만약 j가 맨 처음(0), 마지막(len(d[i])-1)이라면 그냥 바로 위의 값을 더하면 된다.
        if j==0:
            d[i][j]+=d[i-1][j]
        elif j==len(d[i])-1:
            d[i][j]+=d[i-1][j-1]
        # 가장자리 부분이 아니라면 왼쪽, 오른쪽 대각선 위 중 최댓값을 계속 더해나가면 된다.
        else:
            d[i][j]+=max(d[i-1][j-1],d[i-1][j])

print(max(d[n-1]))
