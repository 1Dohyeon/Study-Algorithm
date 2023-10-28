import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    d=[[0 for i in range(3)] for i in range(n+1)]    # d[i][0] 아무것도 뜯지 않음, d[i][1] 위에것을 뜯음, d[i][2] 아래것을 뜯음
    d_1=list(map(int,sys.stdin.readline().split()))
    d_2=list(map(int,sys.stdin.readline().split()))

    for i in range(1,n+1):
        d[i][1]=d_1[i-1]
        d[i][2]=d_2[i-1]

# 경우의 수가 아닌 최댓값을 d에 담는다. d[i][0]일 때는 i-1번째 일때 3가지 경우의 수가 다 되기 때문에 3가지 중 max값을 계속 더하고
# d[i][1]일때는 d[i][0], d[i][2]의 경우가 가능하기에 이 둘중에 max값을 계속 더한다.
# d[i][2]일때는 d[i][0], d[i][1]의 경우가 가능하기에 이 둘중에 max값을 계속 더한다.

    for i in range(2,n+1):
        d[i][0]+=max(d[i-1][0],d[i-1][1],d[i-1][2])  
        d[i][1]+=max(d[i-1][0],d[i-1][2])
        d[i][2]+=max(d[i-1][0],d[i-1][1])

    print(max(d[n]))


    
