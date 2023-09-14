a,m,d,n=map(int,input().split())
sum=int(a)
for i in range(1,n):
    sum *= m
    sum += d
print(sum)
