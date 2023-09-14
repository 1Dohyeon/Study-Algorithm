'''먼저 경우의 수를 n=5일 때까지 구해보면 이 문제의 수열은 피보나치의 수와 유사하단 것을 알 수 있다. 하지만 아래와 같이
피보차이의 수 소수코드를 이용하게 되면 n+1의 값이 정답이란 것을 알 수 있다. 그 이유는 피보나치의 수에서 첫번째 수열의 값은
0, 두번째가 1인데 이 문제에서 첫번째 수열이 1이고 0은 없다고 기준을 놔두었기 때문이다.'''

'''
n=int(input())
memo=[0]*(n+1)  # [0]*n으로 둘 경우 피보나치의 수 n번째가 아닌 n-1번째까지만 배열에 담겨 문제를 풀 수 없다.

def fibonacci2(n):
    if n<=1:
        return n
    else:
        if memo[n]>0:   
            return memo[n]  

        memo[n]=fibonacci2(n-1)+fibonacci2(n-2) 
        return memo[n]

print(fibonacci2(n)%10007)
'''

'''
그리고 아래는 재귀함수를 이용한 Top-down 형식의 문제풀이이다. 반복문을 이용한 Bottom-up 형식으로 문제를 푸는 것이 좋다.
'''

'''
n=int(input())
memo=[0]*(n+1)  

def fibonacci2(n):
    if n<=3:    # 기존의 피보나치 공식이었으면 n=0일 때 0, 1일 때 1, 2일 때 1, 3일 때 2 ...이런식이었지만
                # n<=3일때 n을 return시키므로서 n=0일 0, 1일 때 1, 2일 때 2, 3일 때 3으로 피보나치의 수와는 다른 초반 
                # 조건을 만족시켜줌으로서 위에서 나는 오류를 고쳤다.
        return n
    else:
        if memo[n]>0:   
            return memo[n]  

        memo[n]=fibonacci2(n-1)+fibonacci2(n-2) 
        return memo[n]

print(fibonacci2(n)%10007)
'''

'''
위는 재귀함수를 이용한 Top-down 형식의 문제풀이이다. 위의 풀이도 정답이지만
반복문을 이용한 Bottom-up 형식으로 문제를 푸는 것이 좋다.
'''

n=int(input())
memo=[0]*(n+1)  # 위처럼 memo[0]=0이기 때문에 n+1 크기의 배열을 선언해야 한다.

if n<=3:    # 위의 조건처럼 n<=3일 때 n의 값을 출력한다
    print(n)
else: 
	memo[1]=1
	memo[2]=2
	for i in range(3,n+1):
		memo[i]=memo[i-1]+memo[i-2]

	print(memo[i]%10007)