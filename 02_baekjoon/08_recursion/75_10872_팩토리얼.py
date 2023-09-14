n=int(input())

def factorial(n):
    result=1    # 0팩토리얼은 1이다

    if n>0:
        result=n*factorial(n-1)
    return result

print(factorial(n))

'''일반 팩토리얼
n=int(input())
result=1

if n>0:
    for i in range(1,n+1):
        result*=i

print(result)

'''
