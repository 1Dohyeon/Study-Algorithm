N=int(input())
y=n=0

for i in range(N):
    vote=int(input())
    if(vote==1):
        y+=1
    elif(vote==0):
        n+=1

if(y>n):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
