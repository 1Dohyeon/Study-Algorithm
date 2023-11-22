import sys

n=int(sys.stdin.readline())
a=[0]

for i in range(n):
    a.append(int(sys.stdin.readline()))

d=[0]
d.append(a[1])

if n>1:
    d.append(a[1]+a[2])
for i in range(3,n+1):
    d.append(max(d[i-1],d[i-3]+a[i-1]+a[i],d[i-2]+a[i]))

print(d[n])