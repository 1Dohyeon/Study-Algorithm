n=int(input())

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(n))


'''일반 피보나치의 수
n=int(input())
fibonacci=[0, 1]

for i in range(2,n+1):
    result=fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(result)

print(result)
'''

