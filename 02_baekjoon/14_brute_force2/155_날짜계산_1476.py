import sys

e,s,m=map(int,sys.stdin.readline().split())
a,b,c=1,1,1
cnt=1
while True:
    if a==e and b==s and c==m:
        print(cnt)
        break
        
    a+=1
    b+=1
    c+=1
    cnt+=1

    if a>15:
        a-=15
    if b>28:
        b-=28
    if c>19:
        c-=19

