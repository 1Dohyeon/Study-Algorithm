A,B=map(int,input().split())
C=int(input())

B1=(B+C)%60
A1=(B+C)//60
A2=(A+A1)%24

print(A2,B1)

''' 아래처럼 해도 맞음
N=A*60+B+C

A=N//60
B=N%60

if(A>=24):
    A-=24

print(A,B)
'''
