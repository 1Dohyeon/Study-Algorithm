import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
rvs_a=a[::-1]   # 수열의 역순

inc=[1 for i in range(n)] # LIS
dec=[1 for i in range(n)] # LDS

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            inc[i]=max(inc[i],inc[j]+1)
        if rvs_a[i]>rvs_a[j]:
            dec[i]=max(dec[i],dec[j]+1)

# LIS LDS문제처럼 가장 긴 증가, 감소 부분 수열을 각각 구한다.

result=[0 for i in range(n)]
# 앞과 뒤에서 부터 출발하여 합을 더한다음 1을 빼고 그 중 최댓값을 선택한다
for i in range(n):
    result[i]=inc[i]+dec[n-1-i]-1 # -1을 하는 이유는 i에 속한 기준이 되는 숫자가 중복되는 것을 방지하기 위함

print(max(result))