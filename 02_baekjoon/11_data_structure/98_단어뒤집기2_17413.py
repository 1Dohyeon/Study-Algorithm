import sys

strInput=list(sys.stdin.readline().rstrip())    # 입력받는 값의 오른 쪽에 공백이 있다면 제거 후 입력받는다.
strInput.append(' ')    # 그 후 공백을 추가한다. 
                        # 공백을 추가하는 이유는 마지막에 오는 문자가 태그밖의 문자라면 그것을 pop해야하는데 pop 조건이
                        # i가 ' '이거나 '<'이어야하기 때문이다.
stack=[]    # 문자를 뒤집어 출력하기 위한 스택
tagFlag=False   # true라면 tag사이에 있다는 의미이고 false이면 tag밖에 있단 의미이다.

for i in strInput:  # 입력된 문자 처음부터 끝까지 다 살펴보므로 시간복잡도는 n이다
    if i=='<':  # tag가 열린다면 그 이후의 문자는 그대로 출력해야하므로 
        while stack:    # 그 전의 문자들을 모아둔 stack의 사이즈가 0이 될 때까지 
            print(stack.pop(), end='')  # stack을 print(pop)하여 tag가 열리기 전 문자들을 뒤집어 출력한다.
        tagFlag=True    # tag가 열렸기 때문에 true로 바꿔주고
        print('<', end='')  # 여는 태그를 출력한다.
    elif i=='>':    # 닫는 태그가 입력되었다면
        tagFlag=False   # tagflag를 false로 바꾸어주고
        print('>', end='')  # 닫는 태그를 출력한다.
    elif i==' ':    # 입력 받은 문자가 ' '라면 
        if tagFlag: # 우선 두가지 경우로 나뉘어야 한다. tag안에서의 ' '라면, 즉 tagflag가 true라면
            print(' ', end='')  # 그대로 ' '를 출력한다.
        else:   # false라면
            while stack:    # 그 전에 쌓아둔 태그 밖의 문자들을 뒤집기 위해 반복문을 통하여
                print(stack.pop(), end='')  # print(pop)해준다.
            print(' ', end='')  # 그 이후에 입력된 ' '를 출력한다.
    else:   # 위와 같이 '<'도 아니고 '>'도 아니고 ' '도 아니라면, 즉 1,2,3,a,b,c...와 같은 문자라면
        if tagFlag: # 이 또한 tagflag가 true인지 false인지 두가지 경우의 수를 나누고 우선 true라면
            print(i, end='')    # 태그 안에 문자가 있다는 의미이므로 그대로 i를 출력해주고
        else:   # false라면
            stack.append(i) # 나중에 stack이 끝나고 ' '나 '<'가 올 때 뒤집기 위해 stack에 i를 그대로 쌓아둔다.
