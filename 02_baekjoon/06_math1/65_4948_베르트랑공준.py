'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
'''

''' 시간초과 걸림
while True:
    n=int(input())
    count=0

    if n==0:
        break

    for i in range(n,2*n+1):
        if i==1:
            print(1)
            pass
        else:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                count+=1
    if n!=1:
        print(count)
'''
    
# 시간초과가 걸리므로 문제에 있는 범위를 입력한다.

def case(x):    # x를 매개변수로 하는 함수 case를 만든다.
    if x==1:    # 1은 소수가 아니므로 false를 반환
        return False
    for i in range(2,int(x**0.5)+1):    # 제곱근이 있는 수 중에 약수가 있다면 false를 반환
        if x%i==0:  
            return False
    return True # 그 외는 소수라는 의미이므로 true를 반환

s=[]

for i in range(2,246912+1): # 123456*2=246912이다
    if case(i):
        s.append(i) # case함수에 해당하면 s에 추가

while True:
    n=int(input())
    count=0

    if n==0:
        break   # n=0일 때 아웃하는 것이 문제 조건

    for i in s: # s 리스트 중에서 n범위에서 값이 있으면 count+=1
        if n<i<=2*n:
            count+=1
    
    print(count)
    