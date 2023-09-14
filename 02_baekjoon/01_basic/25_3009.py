x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=0,0
if(x1<1 or y1<1 or x2<1 or y2<1 or x3<1 or y3<1):
    print('좌표는 1보다 크거나 같아야합니다.')
elif(x1>1000 or y1>1000 or x2>1000 or y2>1000 or x3>1000 or y3>1000):
    print('좌표는 1000보다 작거나 같아야합니다.')
else:
    if (x1==x2):
        x4=x3
    elif  (x2==x3): 
        x4=x1
    elif (x1==x3): 
        x4=x2

    if (y1==y2):
        y4=y3
    elif  (y2==y3): 
        y4=y1
    elif (y1==y3): 
        y4=y2

    print(x4,y4)