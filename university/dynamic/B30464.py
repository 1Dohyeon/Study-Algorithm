import sys

a = [0 for i in range(200001)]
dp = [0 for i in range(200001)]

n = int(sys.stdin.readline())
a[:n] = map(int, sys.stdin.readline().split())

# 첫 칸의 수만큼 이동했을 때 등굣길(n)을 벗어나지 않을 경우
if a[0] < n:
    dp[a[0]] = 1

# process 1: 0 ~ n-1 각각의 칸에서 현재 칸에 올 수 있는 방법이 있고(dp[i]!=0),
# 현재 칸에서 a[i]만큼 이동했을 때 등굣길(n)을 벗어나지 않는다면
# dp[i]+1 과 dp[i+a[i]] 중 이동한 칸에 둘 중 더 큰 값을 넣는다.
for i in range(n-1):
    if dp[i]!=0 and i+a[i]<n:
        dp[i+a[i]] = max(dp[i]+1, dp[i+a[i]])

# process 2
# process 1과 달리 n-2부터 0까지 순회한다는 점을 빼면 동일하다
# 즉, 바라보는 방향을 한 번 반전하고 이동하는 것과 같다
for i in range(n-2, 0, -1):
    if dp[i]!=0 and i-a[i]>=0:
        dp[i-a[i]] = max(dp[i]+1, dp[i-a[i]])

# process 3
# process 1과 동일하다
for i in range(n-1):
    if dp[i]!=0 and i+a[i]<n:
        dp[i+a[i]] = max(dp[i]+1, dp[i+a[i]])

# dp[n-1], 학교까지 오는데 드는 시간이 0이 아니라면 dp[n-1]을 출력한다
# 그게 아니라면 -1을 출력한다
if(dp[n-1]!=0):
    print(dp[n-1])
else:
    print(-1)