n=int(input())
result=0

for i in range(1,n+1):
    result=i+sum(map(int,str(i)))
    if result==n:
        print(i)
        break
else:
    print(0)