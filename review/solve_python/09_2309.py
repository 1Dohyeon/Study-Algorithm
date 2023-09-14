import sys

tall=[]

for i in range(9):
    tall.append(int(sys.stdin.readline()))

for i in range(len(tall)-1):
    for j in range(i+1,len(tall)):
        x=tall[i]
        y=tall[j]
        tall[i],tall[j]=0,0

        if sum(tall)==100:
            tall.remove(0)
            tall.remove(0)
            tall.sort()
            for k in tall:
                print(k)
            break
        else:
            tall[i]=x
            tall[j]=y


