M=int(input())  # M<=N
N=int(input())
k=[]

for i in range(M,N+1):
    r=0

    if i==1:
        continue

    for j in range(2,i):
        if i%j==0:
            r+=1
    if r==0:
        k.append(i)

if len(k)==0:
    print(-1)
else:
    print(sum(k))
    print(min(k))

'''
for i in range(M,N+1):

    if i==1:
        continue

    for j in range(2,i):
        if i%j==0:
            break
        
    else:
        k.append(i)

if len(k)==0:
    print(-1)
else:
    print(sum(k))
    print(min(k))

'''

