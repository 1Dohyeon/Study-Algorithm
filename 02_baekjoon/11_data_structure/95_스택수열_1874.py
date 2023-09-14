n=int(input())
stack=[]
result=[]
cnt=1
bool=True

for i in range(n):
    num=int(input())

    while cnt<=num: # 스택 배열에 담길 수 cnt를 1부터 늘려가며 num보다 커지기 전까지 반복
        stack.append(cnt)   # cnt를 스택 배열에 push한다.
        result.append('+')  # push 할 때마다 문제 조건에서는 +를 출력하라 했기에 출력할 result배열애 + push
        cnt+=1  # cnt를 1씩 늘려 다음에는 그 값을 스택배열에 push한다.
    
    if stack[-1]==num:  # 그러다가 스택 배열의 마지막 원소가 입력한 값과 같아지면
        stack.pop() # 스택 배열의 top을 pop해준다.
        result.append('-')  # pop했을 시 문제 조건은 -를 출력하라 했기에 result배열에 - push

    else:   # stack의 top이 입력받은 수와 다르다는 것은, 스택의 top이 입력받은 수보다 크기에 입력받은 수는
            # stack의 아래쪽에 쌓여있기에 배열을 완성시킬 수 없으므로 bool에 false값을 넣어서
        bool=False

if bool==False:
    print('NO') # 배열을 만들 수 없다는 의미로 NO를 출력
else:  
    for i in result:    # 배열을 만들 수 있다면 result 배열을 한줄씩 출력한다.
        print(i)
        