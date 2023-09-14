N,K=map(int,input().split())
coins=[]
count=0

for i in range(N):
    coins.append(int(input()))

for i in range(N-1,-1,-1): # N-1번부터 -1만큼 -1+1번째까지
    count+=K//coins[i]
    K%=coins[i]

print(count)