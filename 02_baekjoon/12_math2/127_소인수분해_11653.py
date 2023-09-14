import sys

n=int(sys.stdin.readline())
i=2 # 소인수분해 스타트는 2부터이므로 i의 기본값을 2로 선언하고

while n>1:  # n이 1보다 크다면 아래절을 계속 반복한다.
    if n%i==0:  # n이 i로 나뉜다면 소인수분해가 된다는 의미이므로
        n//=i   # n은 i로 나눈 값으로 다시 바꿔주고
        print(i)    # 그때의 i를 출력한다.
    else:   # 소인수분해가 되지 않는다면
        i+=1    # i에 1을 더해가면서 소인수분해를 한다.

''' 아래도 비슷한 방법으로 구현한 것이다. 아래 알고리즘 계산이 더 빠르다. 위는 소인수분해가 안돼도 반복이지만 아래는
소인수분해가 되지 않으면 반복을 안해버리고 다음으로 넘어가기 때문인거 같음.

import sys

n=int(sys.stdin.readline())
k=[]

for i in range(2,n+1):
    while n%i==0:
        n//=i
        k.append(i)
    
for i in k:
    print(i)

'''