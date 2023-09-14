t=int(input())

for _ in range(t):
    vps=list(input())
    stack=[]

    for i in vps:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')

'''
t=int(input())

for _ in range(t):
    vps=list(input())
    stack=[]

    for i in vps:
        if i=='(':
            stack.append(i)
        elif i==')' and stack:
            stack.pop()
        elif i==')' and len(stack)==0:  # stack[-1]=='('으로 조건을 뒀을 경우 에러가 뜸. stack에 아무것도 없을 경우
                                        # stack[-1]이 대입될 수 없으므로 에러가 뜨는 거 같음
            print('NO')
            break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')
'''