import sys

def sosu(x):    # 앞 문제 1978에서 for else를 통해 for의 조건이 true인지 false인지 나누고 false이면 else를 실행하는 
                # 방법을 이용했다. 따라서 true or false를 return하는 함수를 이용하여 푸는 것이 시간복잡도 면에서 더 좋다.
                # for else는 false인지 true인지 내놓는거 뿐만 아니라 계산까지 해야하기 때문이다.
    if x==1:
        return False    # 1은 소수가 아니므로 false
    for i in range(2,int(x**0.5)+1):
        if x%i==0:  # 무언가로 나누어 떨어지면 소수가 아니므로
            return False    # false를 return
    return True # 위 모든 경우의 수가 아니라면 소수이므로 true를 return

m,n=map(int,sys.stdin.readline().split())
sosu_list=[]

for i in range(m,n+1):
    if sosu(i): # 위에 만든 sosu함수가 true라면 그때의 i는 소수이므로
        sosu_list.append(i) # 소수 리스트에 담는다.

for i in sosu_list:
    print(i)


