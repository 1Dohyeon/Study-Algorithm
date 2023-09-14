N=int(input())
P=list(map(int,input().split()))
P.sort()

# def란 함수를 지정하는 것이다. def 함수이름(): 을 입력한 뒤 원하는 함수를 만들고, 함수이름()을 통해서 실행시킨다. 
def solution1():
    result=0
    for i in range(N):
        for j in range(i+1):    # range(i)로 두면 i-1까지 이므로 i+1까지로 범위를 지정한다.
            result+=P[j]
    print(result)

def solution2():    # solution2와 같은 방식이 시간을 덜 잡아먹는다.
    result=0
    for i in range(N):
        result+=sum(P[0:i+1]) # P의 0번째부터 i번째 수까지의 합을 result에 담는다. sum함수 이용
    print(result)

solution2()
