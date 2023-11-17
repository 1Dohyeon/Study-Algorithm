h,m=map(int,input().split())
n=int(input())
M=m+n

while M>=60:
    
    if M>=60:
        M-=60
        h+=1

        if h>=24:
            h-=24

print(h,M)