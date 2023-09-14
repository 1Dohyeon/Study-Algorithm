A,B,C=map(int,input().split())
D=int(input())

C1=(C+D)%60 #최종 초
B1=(C+D)//60
B2=(B+B1)%60 #최종 분
A1=(B+B1)//60
A2=(A+A1)%24 #최종 시각

print(A2,B2,C1)

''' 아래거도 실행할 경우 맞는데 왜 안되는지 모르겠음;;
N=A*3600+B*60+(C+D)
N=int(N)

A=N//3600
B=(N-A*3600)//60
C=N%60

if(A>=24):
    A-=24

if(B>=60):
    B-=60

print(A,B,C)
'''