case=int(input())

for i in range(case):
    q=list(input())
    result=0
    score=1

    for j in range(len(q)):
        if q[j]=='O':
            result+=score
            score+=1
        else:
            score=1
        
    print(result)

