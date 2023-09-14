n=int(input())  # 도시 수, 주유소 수
km=list(map(int,input().split()))   # 도시간의 거리, 원소 갯수=도시 수 -1
cost=list(map(int,input().split()))    # 기름 가격, 원소갯수=도시 수
min_cost=cost[0]
result=0

for i in range(n-1):    # 마지막 도시에서는 기름을 넣을 필요가 없기 때문에 범위를 0~n-2까지로 지정
    if min_cost>cost[i]:
        min_cost=cost[i]
        result+=min_cost*km[i]
    else:
        result+=min_cost*km[i]

print(result)






