N=int(input())
sum=0

for i in range(N):
    r,e,c=map(int,input().split())
    sum=e-r
    if(sum>c):
        print('advertise')
    if(sum==c):
        print('does not matter')
    if(sum<c):
        print('do not advertise')