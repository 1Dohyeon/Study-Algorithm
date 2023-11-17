# Last In First Out, 마지막에 들어간 것이 가장 먼저 나온다. 

''' 위처럼 스택이란 여러개를 입력받을 경우 마지막에 입력받은 것만 의미가 있을 경우에 사용된다. '''
import sys

stack=[]
n=int(sys.stdin.readline()) # input으로 입력받으면 시간초과에 걸린다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

for i in range(n):
    comd=sys.stdin.readline().split()   # 지금까지 한 개의 매개변수에 split()함수를 이용할 때 list를 이용했지만
                                        # list없이도 split을 통해 list형식으로 매개변수를 선언할 수 있다.

    if comd[0]=='push':
        stack.append(comd[1])

    elif comd[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())  # pop()함수는 배열의 마지막 원소를 지우는 것이며 print와 pop을 두 줄로 나누어 적지 않고
                                # 이와 같이 적으면 한줄로도 마지막 원소를 print 후 pop 시킬 수 있다.

    elif comd[0]=='size':
        print(len(stack))
    
    elif comd[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
    elif comd[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])    # 배열의 마지막 번째를 'len(배열)-1'로 하기보단 '-1'로 나타낼 수 있다.

