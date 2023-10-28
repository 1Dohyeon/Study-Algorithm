N = int(input())
P = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    
    if a == b == c: #2번 연속 == 가능
        P = max(P, 10000+a*1000)
    elif a == b:
        P = max(P, 1000+a*100)
    elif a == c:
        P = max(P, 1000+a*100)
    elif b == c:
        P = max(P, 1000+b*100)
    else:
        P = max(P, 100 * max(a,b,c))

print(P)