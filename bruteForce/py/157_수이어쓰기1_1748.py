import sys
input=sys.stdin.readline

n=input().rstrip()

'''
num=1
num=str(num)

for i in range(2,n+1):
    num+=str(i)

print(len(num))

위 방법에서는 시간초과가 뜬다.
'''

# 한자릿수의 총합은 9(9가지*자릿수(1))
# 두자릿수의 총합은 180(90가지*자릿수(2))
# 세자릿수의 총합은 2700(900가지*자릿수(3)) 의 규칙을 가지고 있음.

cnt=0

# for문을 통해 위와같이 자릿수 단위로 끊은 최댓값을 더해줌.
# 예를 들어 n=120일때 len(n)=3이고 아래 반복문은 i=1,2로 탐색한다.
for i in range(1,len(n)):
    cnt+=int('9'+(i-1)*'0')*i   # i=1일 때 9*1=9(한자릿수 총합)
                                # i=2일 때 '9'+1 * '0' = '90' --> int --> 90 * 2 = 180(두자릿수 총합)
# 위 식을 통해 cnt=189가 되었고, 이제 나머지 100부터 120까지의 세자릿수 합을 계산해준다.
cnt+=(int(n)-10**(len(n)-1)+1)*len(n) 

print(cnt)

