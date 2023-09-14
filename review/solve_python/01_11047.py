n, k = map(int,input().split()) # N(동전 종류의 갯수), K(만들어야할 금액)

coins = []  # 동전의 종류
for _ in range(n):
    coins.append(int(input()))

cnt = 0     # 필요한 동전의 최솟값
for i in range(n-1,-1,-1):
    cnt += k//coins[i]
    k %= coins[i]
    if k==0:
        print(cnt)
        break

