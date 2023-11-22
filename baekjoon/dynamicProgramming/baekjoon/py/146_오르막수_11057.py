import sys

n=int(sys.stdin.readline())
# d[i][j]는 i번째 자리에 j가 들어갈 경우의 수
d=[[0 for i in range(10)] for i in range(n+1)]

for i in range(10):
    d[1][i]=1

# d[i][j]는 d[i-1][0]~d[i-1][j]까지의 경우의 수의 합이다. 즉 d[i][j-1]은 d[i-1][0]~d[i-1][j-1]의 합이다. 이 뜻은
# d[i][j]는 결국 d[i][j-1]과 d[i-1][j]의 합이다. 표로 보면 쉽게 직관할 수 있다.

for i in range(2,n+1):
    for j in range(10):
        if j==0:    # j=0이면 경우의 수는 0000 ... 0 이라는 경우 1개밖에 없다.
            d[i][j]=1
        else:
            d[i][j]=d[i-1][j]+d[i][j-1]

print(sum(d[n])%10007)

