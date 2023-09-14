a,b,c=map(int,input().split())

if(a==b and b==c):
    print(10000+a*1000)
elif((a==b and b!=c)or(a==c and a!=b)):
    print(1000+a*100)
elif(b==c and b!=a):
    print(1000+b*100)
elif(a!=b and a!=c and b!=c):
    print(100*max(a,b,c)) #max는 최댓값을 구하는 함수이다
    
''' max함수가 있지만 if-else를 통해서 max를 구함
max=(a if (a>b) else b) if ((a if (a>b) else b)>c) else c
print(max)
'''