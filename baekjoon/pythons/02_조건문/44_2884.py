h,m=map(int,input().split())
M=m-45

if M<0:
    M+=60
    h-=1

    if h<0:
        h+=24

print(h,M)


