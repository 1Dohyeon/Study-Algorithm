n=int(input())
k=[]

for i in range(n):
    x,y=map(int,input().split())
    k.append((x,y))

for i in range(n):
    rank=1
    for j in range(n):
        if k[i][0]<k[j][0] and k[i][1]<k[j][1]:
            rank+=1

    print(rank,end=' ')
        
