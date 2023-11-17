a,b,v=map(int,input().split())
s=a-b   # 하루동안 올라간 높이(그 당일에 최고점까지 도달 못 할 경우)
day=(v-b)/s    
'''올라갈 날의 최솟값, //로 몫을 구하지 않는다. 만약 .n처럼 소수점 자리가 나온다면 하루가 더 걸린다는 의미이므로,
소수점을 없앤 int타입으로 변환 후 +1을 더해준다.'''
print(int(day) if day==int(day) else int(day)+1)



'''
시간초과가 뜬다 

while s<v:
    s+=a
    day+=1
    if s<v:
        s-=b
    
print(day)'''
    