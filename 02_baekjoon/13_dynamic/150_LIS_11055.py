import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
d=[0 for i in range(n)]
d[0]=a[0]

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            d[i]=max(d[i],d[j])
    d[i]+=a[i]  # 기본적으로 자기 자신의 합을 가진다.
print(max(d))