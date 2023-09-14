n=int(input())
s=list(map(int,input().split()))
s.sort()    # 값들을 크기별로 정리하고 왼쪽에서 i번째 값과 오른쪽에서 i번째 값을 더해주면 최솟값의 합이 최대화가 된다.
g=[]

for i in range (n):   
    g.append(s[i]+s[len(s)-1-i])    

print(min(g))