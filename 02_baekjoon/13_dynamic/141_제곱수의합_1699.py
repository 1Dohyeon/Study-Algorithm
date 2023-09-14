import sys

n=int(sys.stdin.readline())
d=[0 for i in range(n+1)]   

for i in range(1,n+1):
    d[i]=i  # i의 제곱수의 합은 1의 제곱으로만 이루어진 경우가 최댓값이므로 그 값인 i로 초기값 지정
    for j in range(1,int(i**0.5)+1):    # 범위를 보면 제곱수의 원소는 절대 루트 i를 넘을 수 없기 때문에 i제곱근까지 범위 지정.
        if d[i]>d[i-j**2]+1:    # a+b+c를 n-1의 제곱근 식으로 둔다면, n의 제곱근 식은 a+b+c+j^2=n이다. 
                                # n-j^2제곱근 식에 1개의 항이 더해진 것이다. 따라서 d[n]=d[n-i^2]+1이다.   
            d[i]=d[i-j**2]+1    # 최솟값을 담아야함으로 위 점화식이 초기값보다 작다면 d[i]에 점화식을 대입한다.

print(d[n])

