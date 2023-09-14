import sys

t=int(sys.stdin.readline())
mod=1000000009
d=[0 for i in range(1000001)]
d[1]=1
d[2]=2
d[3]=4
d[4]=7

for i in range(5,1000001):
    d[i]=d[i-1]%mod+d[i-2]%mod+d[i-3]%mod

for _ in range(t):
    n=int(sys.stdin.readline())
    print(d[n]%mod)
    

    