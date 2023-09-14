import sys

n=int(sys.stdin.readline())
mod=9901
# d[i][0]: i번째 칸에 동물x, d[i][1]: i번째 칸 왼쪽에 동물, d[i][2]: i번째 칸 오른쪽에 동물

d=[[0 for i in range(3)] for i in range(n+1)]

for i in range(3):
    d[1][i]=1

for i in range(2,n+1):
    d[i][0]=d[i-1][0]%mod+d[i-1][1]%mod+d[i-1][2]%mod
    d[i][1]=d[i-1][0]%mod+d[i-1][2]%mod
    d[i][2]=d[i-1][0]%mod+d[i-1][1]%mod

print(sum(d[n])%mod)
