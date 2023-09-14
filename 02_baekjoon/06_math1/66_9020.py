def case(x):    # x를 매개변수로 하는 함수 case를 만든다.
    if x==1:    # 1은 소수가 아니므로 false를 반환
        return False
    for i in range(2,int(x**0.5)+1):    # 제곱근이 있는 수 중에 약수가 있다면 false를 반환
        if x%i==0:  
            return False
    return True # 그 외는 소수라는 의미이므로 true를 반환

test=int(input())

for i in range(test):
    n=int(input())
    
    a=n//2
    b=n//2

    while a>0:
        if case(a) and case(b): # case(a)와 case(b) 둘 다 참이라면
            print(a,b)
            break
        else:
            a-=1
            b+=1
    
    

