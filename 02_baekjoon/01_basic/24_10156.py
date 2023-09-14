K,N,M=map(int,input().split())
need=K*N
if(need-M<0):
    print(0)
else:
    print(need-M)