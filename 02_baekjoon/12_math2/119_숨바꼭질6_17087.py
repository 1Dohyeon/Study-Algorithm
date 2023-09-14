def gcd(a,b):   # 유클리드 호제법으로 최대공약수를 구하는 함수이다. 05_practice_baekjoon_알고리즘기초1-->04_수학1
                # -->02_최대공약수와_최소공배수_2609 참고
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,s=map(int,input().split())    # n은 동생의 수, s는 수빈이의 위치
a=list(map(int,input().split()))    # 동생의 위치
dif=[]    # 수빈이와 동생들의 거리차이

for i in a:
    dif.append(abs(i-s))

''' 아래와 같이 먼저 두 수의 최대공약수를 구하고 그 최대공약수와 다른수의 최대공약수의 최대고약수를 구하는 것이 다수에서
    최대공약수를 구하는 방법이다.

    하지만 문제에서는 동생이 한명인 경우 dif[1]은 존재하지 않기 때문에  if를 통해서 len(dif)=1인 경우를 생각해서 코드를 
    짜야한다.'''

''' 하지만 이 방법보다 코드를 더 깔끔하게 짤 수 있다.
if len(dif)==1:
    print(dif[0])
else:
    k=gcd(dif[0],dif[1])
    for i in range(2,len(dif)):
        k=gcd(k,dif[i])
    print(k)
바로 아래처럼 k=dif[0]이라고만 두고 len(dif)가 1일 때 k만 출력하고 자기 자신과의 최대공약수는 어차피 자기 자신이므로
위처럼 2부터 시작하는 반복문이 아닌 처음부터 반복문을 돌려도 된다.''' 

k=dif[0]
if len(dif)==1:
    print(k)
else:
    for i in range(len(dif)):   # 유클리드 호제법을 이용한 gcd함수를 
        k=gcd(k,dif[i]) # k를 통해서 계속 반복시켜서 다수의 최대공약수를 구한다.
    print(k)

    