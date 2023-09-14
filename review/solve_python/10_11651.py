import sys

n = int(input())
xy = []

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    xy.append([b,a])

xy.sort()

for i in range(n):
    print(xy[i][1],xy[i][0])