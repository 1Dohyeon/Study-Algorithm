case=int(input())


for i in range(case):
    result=list(str(input()))
    total_score=0
    score=0

    for j in range(len(result)):
        if(result[j]=='O'):
            score+=1
            total_score+=score
        else:
            score=0

    print(total_score)
