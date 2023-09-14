H,M=map(int,input().split())
M1=M-45
if(M1<0):
    H-=1
    M1=M1+60
if(H<0):
    H+=24

print(H,M1)