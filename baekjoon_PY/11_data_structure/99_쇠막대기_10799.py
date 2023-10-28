razor=list(input()) 
result=0    # 막대 조각의 갯수
stack=[]

# 문제를 보면 '('다음에 바로')' 나와야 레이저가 발사된다.

for i in range(len(razor)):
    if razor[i]=='(':   # 입력받은 괄호가 열린 괄호라면
        stack.append('(')   # stack에 열린 괄호를 push한다.
    else:   # 열린 괄호가 아니라 닫는 괄호라면,
        if razor[i-1]=='(': # 그리고 바로 전이 열린 괄호라면 레이저를 쏴야하고 그전까지의 막대길이는 스택에 쌓여있는
            stack.pop() # 열린 괄호의 갯수와 같으므로 stack에 top인 열린 괄호를 pop해주고
            result+=len(stack)  # 출력할 결과값에 stack에 그동안 쌓인 열린괄호의 갯수를 담아준다.
        else:   # 닫힌 괄호 이전이 열린괄호가 아니라 닫힌 괄호라면(스택 아님, 입력받은 리스트에서)
            stack.pop() # 스택에 쌓인 top 열린 괄호를 pop 해주고
            result+=1   # 입력받은 리스트에서 닫힌 괄호 전이 닫힌 괄호라면 막대기의 끄트머리 한조각이므로 +1해준다.

print(result)