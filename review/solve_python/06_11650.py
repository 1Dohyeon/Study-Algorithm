import sys

n=int(input())
xy=[]

for _ in range(n):
    a,b=map(int,sys.stdin.readline().split()) 
    xy.append([a,b])

xy.sort()
for i in range(n):
    print(xy[i][0],xy[i][1])
    