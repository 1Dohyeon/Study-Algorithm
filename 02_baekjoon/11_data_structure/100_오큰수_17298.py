import sys

n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
stack=[]    # 원소의 인덱스 값을 가질 스택
nge=[-1]*n  # 수열의 마지막 수는 -1로 고정이고 오큰수가 없을 때는 무조건 -1이기 때문에 nge의 기본값은 -1로 지정한다.
stack.append(0) # 처음 스택에는 수열a 첫번 째 인덱스, 즉 0을 push한다.

for i in range(1,len(a)):
    while stack and a[stack[-1]]<a[i]:  # 스택이 존재하고, a의 i번째 수가 스택에 top에 있는 수를 인덱스로 두는
        nge[stack.pop()]=a[i]   # a보다 크다면 stack의 top을 인덱스로 두는 nge의 원소에 a[i]를 push한다.
    stack.append(i) # 위 while 문이 실행되지 않을 경우or실행 된 후, stack에 원소값이 아닌 원소의 인덱스 값을 넣어준다.    

print(*nge) # *리스트를 이용하여 리스트 형식을 한 칸씩 띄워서 출력한다.


# 아래는 stack의 pop을 이용하지 않고 for만 이용하여 푼 방법이다. 단 시간초과에 걸린다.

''' 두 개의 for문으로 수열을 돌기 때문에 시간복잡도가 n^2가 되어 시간 초과에 걸린다.
import sys

n=int(sys.stdin.readline()) # 입력 속도를 줄이기 위해 sys.stdin.readline을 이용
a=list(map(int,sys.stdin.readline().split()))   # 수열을 리스트 형태로 입력받는다.
nge=[]

for i in range(n):
    for j in range(i+1,n):
        if a[j]>a[i]:   # 리스트 한개를 고정시키고 그 다음번째 원소들을 반복시켜서, 만약 그 뒤에 숫자가 크다면
            nge.append(a[j])    # nge에 그 수를 담고
            break               # 반복문을 바로 탈출한다.
    else:   # 조건문의 결과가 false라면 큰 수가 없단 의미이므로  
        nge.append(-1)  # nge에 -1을 담는다

print(*nge) # *리스트를 이용하여 리스트 형식을 한 칸씩 띄워서 출력한다.
'''