P=int(input())
for i in range(P):
    a,b=input().split()
    a=int(a)
    b=str(b)
    for j in range(len(b)):
        print(b[j]*a, end='')
    print()