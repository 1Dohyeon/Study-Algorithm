A,B,C=map(int,input().split())

'''(a+b)%c = ((a%c)+(b%c))%c 이다.  +가 아닌 빼기도 성립하지만 a-b가 음수일 경우 프로그래밍 언어에 따라 결과값이
다르다.'''

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)