'''n-m=r일때 nCm=n!/(n-m)!*r! 이다. 예를 들어 10C5일 때 답은 3628800/(120*120)이고 이를 소인수 분해 해보면 
조합 0의 개수는 2의 지수와 5의 지수 중 작은 값으로 결정된다. 
즉 nCm에서 2의 지수는 n!의 2의 지수-((n-m)!에서의 2의 지수+r!의 2의 지수)이고 5도 이와 같이 구한 후 작은 값을 출력한다.'''

# 먼저 지수를 알 수 있는 함수를 만든다.
def cnt_num(n,k):
    cnt=0
    while n>0:  # n팩토리얼에서 k의 지수를 구하는 방법, 07_팩토리얼0의개수_1676참고
        n//=k
        cnt+=n
    return cnt

n,m=map(int,input().split())

cnt5=cnt_num(n,5)-(cnt_num(n-m,5)+cnt_num(m,5))
cnt2=cnt_num(n,2)-(cnt_num(n-m,2)+cnt_num(m,2))

print(min(cnt5,cnt2))