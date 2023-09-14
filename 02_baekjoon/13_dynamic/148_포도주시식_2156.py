import sys

n=int(sys.stdin.readline())
a=[0]

for i in range(n):
    a.append(int(sys.stdin.readline()))

d=[0]
d.append(a[1])

if n>1:
    d.append(a[1]+a[2])

for i in range(3,n+1):
    # 세개를 연속적으로 선택할 수 없다.
    # 즉            
    # 첫 번째 경우는 i번째를 선택안하는 i-1번째 경우
    # i-3번째까지의 경우에서 3개이상이 겹치지 않게 한칸 띄우고 a[i-1], a[i]의 경우
    # i-2번째까지의 경우에서 한칸 띄우고 a[i]만 선택한 경우
    # 로 나눌 수 있다. 그 중에 최댓값을 선택하면 된다.
    d.append(max(d[i-1],d[i-3]+a[i-1]+a[i],d[i-2]+a[i]))
    
print(d[n])  