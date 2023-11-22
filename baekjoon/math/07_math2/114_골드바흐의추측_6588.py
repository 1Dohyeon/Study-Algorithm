import sys

def sosu_f(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    for i in range(3,n+1,2):    # 문제에서 범위는  6부터이므로 6의 소수합은 3+3이므로 3부터 n까지(n+1로 선언)
                                # 짝수만큼(소수는 홀수이므로 홀수+짝수=홀수를 이용하여 반복횟수를 줄인다) 증가시켜서 
                                # 반복한다.
        if sosu_f(i):   # 작은 수부터 차례로 소수를 찾고 소수가 나온다면
            if sosu_f(n-i): #  그때 n-i가 소수라면 두 소수의 합은 n이면서 소수중에 가장 멀기 때문에
                print(n,'=',i,'+',n-i)  # 그 값을 출력하고
                break   # 반복문을 빠져나온다.