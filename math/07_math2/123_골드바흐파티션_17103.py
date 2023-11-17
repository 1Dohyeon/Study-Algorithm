import sys

''' 시간초과가 뜬다.

def sosu_f(x):  # 에라토스테네스의 체
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True


t=int(sys.stdin.readline())

for i in range(t):
    num=int(sys.stdin.readline())
    cnt=0

    for j in range(2,num//2+1):
        if sosu_f(j) and sosu_f(num-j):
            cnt+=1

    print(cnt)'''

sosu=[] # 소수를 담을 리스트
check=[True]*1000001    # 문제에서 주어진 범위만큼 소수인지 아닌지 판별할 배열. True이면 소수 아니면
check[0]=False
check[1]=False   # 0과 1처럼 False이다.

for i in range(2,1000001):
    if check[i]==True:  # check배열에서 True라면 소수라는 의미이므로
        sosu.append(i)  # sosu배열에 담고
        for j in range(i+i,1000001,i):  # 소수의 두배, 즉 i+i부터 문제에서 지정한 범위인 1000001까지 i크기만큼 증가시키면
                                        # i의 배수라는 것, 즉 소수가 아니란 의미이므로  
            check[j]=False  # False값을 가지게 한다.

t=int(sys.stdin.readline())

for i in range(t):
    cnt=0
    n=int(sys.stdin.readline())

    for i in sosu:  # 2부터 1000001까지 소수들이 모여있는 배열에서 작은 수부터 반복시킨다
        if i>=n//2+1:   # 3,5 그리고 5,3은 같으므로 반까지만 계산하면 된다. 
                        # 따라서 입력받은 수의 절반이 소수 배열에 있는 원소보다 작을 경우 입력받은 수 내에서
            break   # 계산이 끝났다는 의미이므로 반복문을 빠져나온다.
        if check[n-i]: # i는 소수임이 확정이므로 n-i까지 소수일 경우
            cnt+=1  # 카운트를 세어준다.

    print(cnt)