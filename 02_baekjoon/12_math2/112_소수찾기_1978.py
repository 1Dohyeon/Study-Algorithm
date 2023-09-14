n=int(input())
sosu=list(map(int,input().split()))
cnt=0

for i in sosu:
    if i==1:
        continue

    for j in range(2,int(i**0.5)+1):    # 약수의 대칭을 이용하여 제곱근까지만 반복하여 소수를 구하는 기본 방법이다.
        if i%j==0:
            break
    else:   # 만약 for 조건문이 false라면, break되지 않는다면 소수라는 의미이므로
        cnt+=1  # cnt에 1을 더해준다.

print(cnt)