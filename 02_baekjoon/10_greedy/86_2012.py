'''
N=int(input())
S=[]

# 한번에 쳐서 split을 하고 배열에 담는 방식이 아니기 때문에 for문으로 배열에 담는다
for i in range(N):
    S.append(int(input()))  

S.sort()
result=0

for i in range(N):  # 0부터N-1까지
    result += abs((i+1)-S[i])   # i는 0부터N-1까지이기 때문에 등수는 1등부터 이므로 i+1, S는 배열이기에 젤 작은 수인 0번째 원소부터 시작

print(result)   

# 시간초과가 뜬다...
'''

import sys  # sys 모듈을 불러온다.

N = int(sys.stdin.readline())   # sys모듈에서의 int타입 입력값을 받는 법=(sys.stdin.readline())
S = [int(sys.stdin.readline()) for i in range(N)]  # int타입 입력값을 반복함수를 이용하여 0부터 N-1번까지 총 N번 입력받는다.

# 각 사람이 예상한 등수를 오름차순으로 정렬한다.
S.sort()
# 랭크를 사람의 수만큼 만든다.
rank = [i for i in range(1, N+1)]   # range(N)이라고 할 경우에는 0부터 n-1까지이므로 0등에서 n-1등까지만 생긴다. 따라서 1,N+1로 범위를 선정한다.
# 불만도 최소합
result = 0

# 랭크에서 각 사람이 예상한 등수를 빼면 불만도에 최소를 구할수있다.
for i in range(N):
    result += abs(rank[i] - S[i])   # abs는 절댓값이다.

print(result)

# 위처럼 시간초과가 뜬다면 sys모듈을 이용하여 풀면 된다.

