n=int(input())
d=[[0 for i in range(10)] for j in range(101)]  # d[n][L] 일때 길이는 n이고 마지막 숫자는 L

for i in range(1,10):
    d[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j]=d[i-1][1]   # 길이 하나이므로 경우의 수는 전의 경우의 수와 같음
        elif j==9:
            d[i][j]=d[i-1][8]
        else:
            d[i][j]=d[i-1][j-1]+d[i-1][j+1]

print(sum(d[n])%1000000000)