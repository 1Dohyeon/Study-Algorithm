n=int(input())
score1=list(map(int,input().split()))
score2=[]

for i in range(n):
    score2.append(score1[i]/max(score1)*100)

print(sum(score2)/len(score2))
