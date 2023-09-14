T=int(input())
for i in range(T):
    mars=list(map(str,input().split())) #리스트 선언
    A=0
    for j in range(len(mars)):
        if j == 0:
            A += float(mars[j])
        else:
            if mars[j] == "#":
                A -= 7
            elif mars[j] == "%":
                A += 5
            elif mars[j] == "@":
                A *= 3
    print("%0.2f" % A)