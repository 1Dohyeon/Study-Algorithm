T=int(input())

for i in range(T):
    N=int(input())
    max=0
    winner=''

    for j in range(N):
        S,L=map(str,input().split())
        L=int(L)

        if(L>max):
            max=L
            winner=S
    
    print(winner)
    