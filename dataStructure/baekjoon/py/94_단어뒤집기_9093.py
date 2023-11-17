import sys  

t=int(sys.stdin.readline())

for i in range(t):
    word=sys.stdin.readline().rstrip()
    word+=' '   # 입력받은 word 마지막에 ' '를 붙여줌으로서 마지막 단어도 아래절을 반복할 수 있게 한다.
    stack=[]

    for j in word:  # j를 word 매개변수에 한단어씩 두고 다음 단어로 차례대로 반복한다.
        if j!=' ':  # j가 ' '처럼 띄어쓰기가 아니라면
            stack.append(j) # stack에 담고
        else:   # 띄어쓰기일 때
            while len(stack):   # stack의 size만큼
                print(stack.pop(),end='')   # print 후 pop해주어 입력된 순서의 거꾸로 출력한다. 이 때 출력되는 문자들이
                                            # 띄어쓰기나 줄바꿈이 되지 않게 end=''를 이용한다.
            print(' ',end='')   # stack의 size만큼 반복이 끝났다면 원래 문장처럼 띄어쓰기를 출력한 후 그 뒤에 바로 또
                                # 위의 절이 반복될 수 있게 end=''를 이용한다.

''' sys '''

''' stack, pop을 이용하지 않고 list 내부에서 제공하는 기능을 이용한 풀이

for i in range(t):
    word=input().split()    # 띄어쓰기를 기준으로 나누어 단어를 word배열에 담고

    for j in word:  # word 배열의 첫번째 원소부터 아래를 절을 반복시킨다.
        print(j[::-1],end=' ')  # 원소의 첫번째부터 마지막번째의 문자를 역순으로 출력 후 띄어쓰기로 끝마친다.

위 식이 첫번째 방법보다 시간복잡도가 적다.
'''