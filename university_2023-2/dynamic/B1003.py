# 피보나치 수를 구하는 메서드 = 피보나치에서 1이 호출된 갯수
def fibonacci(n):
    dp = [0, 1, 1]
    zeroCnt = [1, 0, 1]

    # n에 따라 0이 출력되는 횟수인 zeroCnt와 1이 출력되는 횟수인 dp 역시 피보나치 수열의 패턴을 갖는다는 것이 핵심
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
        zeroCnt.append(zeroCnt[i-1] + zeroCnt[i-2])

    print(zeroCnt[n], dp[n])


T = int(input())

for i in range(T):
    n = int(input())
    fibonacci(n)


