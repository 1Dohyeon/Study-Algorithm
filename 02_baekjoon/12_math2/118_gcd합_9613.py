def gcd(a,b): 
    if b==0:
        return a
    else:
        return gcd(b,a%b)

t=int(input())

for _ in range(t):
    num=list(map(int,input().split()))  # num[0]은 수의 개수
    num.pop(0)  # 수의 개수는 최대공약수를 구할 때 필요 없으므로 지워준다. pop()만 한다면 가장 마지막 원소가 지워지지만
                # pop(n)을 하면 n번째 원소가 지워진다.
    result=0  

    for i in range(len(num)-1): # 브루트포스 문제들처럼 한개를 고정시키고 뒤의 숫자들을 전부 비교해야 한다.
                                # i는 마지막까지 갈 필요가 없으므로 len(num)-1까지 범위를 지정하고
        for j in range(i+1,len(num)):   # 비교대상인 j를 마지막번호까지 반복시킨다.
                                        # 하지만 사실상 j가 i+1부터 시작이라 i 범위를 len(num)까지 둬도 상관은 없다.
            result+=gcd(num[i],num[j])
    
    print(result)

