'''for 문

num=int(input())
f=1

for i in range(1,num+1):
    f*=i

print(f)
'''

# 재귀함수
def factorial(x):
    result=1

    if x>1:
        result=x*factorial(x-1)
    return result

num=int(input())

print(factorial(num))
