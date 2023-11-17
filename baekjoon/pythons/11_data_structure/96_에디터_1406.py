import sys

stack1=list(input())    # list(input())을 통해 단어를 한글자씩 나누어 바로 배열에 담는다.
stack2=[]
n=int(input())

for i in range(n):
    comd=sys.stdin.readline().split()   # comd[0]은 명령어, comd[1]은 추가할 문자이다.    

    # comd는 sys를 통해 입력받고, 나머지 stack1이랑 n은 sys로 담으면 에러가 난다. 이유는 모르겠음 sys로 리스트 입력받을 때
    # 마지막 원소는 \n이기 때문ㄴ

    if comd[0]=='L' and stack1: # 명령어가 L이고 stack1이 존재할 경우라는 조건이다.
        stack2.append(stack1.pop())

    # 왜 stack==True라고 적으면 에러가 나는지 모르겠음..

    elif comd[0]=='D' and stack2:
        stack1.append(stack2.pop())

    elif comd[0]=='B' and stack1:   # 문자를 지울 때도 문자가 있어야 하므로 stack1이라는 조건을 추가한다.
        stack1.pop()

    elif comd[0]=='P':
        stack1.append(comd[1])


print("".join(stack1+list(reversed(stack2))))   # reversed를 통해 stack2를 reverse해준다. 
                                                # reversed를 사용하면 다시 list형태로 바꾸어줘야한다. 
                                                # 그 후 .join 함수를 통해 stack1과 stack2를 간격 없이 합쳐준다. 
                                                # ""를 통해 합친 두 배열을 문자열 타입으로 만든다.

# sep를 이용하여 많이 출력하지만 배열같은 경우는 []의 표시도 같이 나오기 때문에 배열을 같이 출력하고 싶을 때는 아래말고
# 위와 같이 "".join(+)함수를 통해 배열을 함께 출력한다.


'''
print(stack1,list(reversed(stack2)),sep='')
'''
# 아래와 같은 방법도 출력할 수 있지만 반복문을 통해 배열을 하나하나 다 읽어내야함으로 시간이 더 오래걸린다.


'''
for i in stack1:
    print(i,end='')
stack2=reversed(stack2)

for i in stack2:
    print(i,end='')'''
