'''   시간초과 나옴
case=int(input())
a=1
for i in range(case):
    A,B=map(int,input().split())
    while(a%A!=0 or a%B!=0):
        a+=1
    print(a)
    a=1
'''

case=int(input())

for i in range(case):
    A,B=map(int,input().split())
    x,y=A,B

    while y!=0:
        temp=x
        x=y
        y=temp%y
    print(A*B//x)