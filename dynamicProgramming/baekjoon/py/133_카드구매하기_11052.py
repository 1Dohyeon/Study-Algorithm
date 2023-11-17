import sys

n=int(sys.stdin.readline())
p=[0]+list(map(int,sys.stdin.readline().split()))   # n개의 카드를 가져야 하기 때문에 계산하기 쉽게 p[0]=0으로 두고 p[1]
                                                    # 부터 입력받는다.
d=[0]*(n+1) # 위에서 언급한것대로 1~n까지 계산해야 하기 때문에 d[0]=0으로 둬야한다. 따라서 n이 아닌 n+1을 곱한다.
d[1]=p[1]   # 1개를 살 경우 당연히p[1]


# d[2] = d[1] + p[1] or d[0] + p[2]
# d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
# d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4] 이다.

# 즉 d[i]는 d[i-1]과 d[1]의 합 또는 d[i-2]와 p[2]의 합. 즉 d[i-j]와 p[j]의 합이 d[i]이다.

for i in range(2,n+1):
    for j in range(1, i+1):
        d[i]=max(d[i],d[i-j]+p[j])  # 하지만 문제의 조건은 최댓값이기 때문에 위 식으로 첫 d[i]를 구하고 다음 d[i]와
                                    # 반복 비교하여 큰 수를 d[i]에 담는다.
print(d[i])
