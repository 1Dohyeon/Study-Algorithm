N,M = map(int, input().split())
original=[]
count=[]

for i in range(N):
    original.append(input())

for i in range(N-7):
    for j in range(M-7):
        index1=0
        index2=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if original[x][y]!='W':
                        index1+=1
                    if original[x][y]!='B':
                        index2+=1
                else:
                    if original[x][y]!='B':
                        index1+=1
                    if original[x][y]!='W':
                        index2+=1
        count.append(min(index1,index2))

print(min(count))
