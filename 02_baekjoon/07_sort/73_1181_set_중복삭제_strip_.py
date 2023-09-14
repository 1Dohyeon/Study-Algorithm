# input()을 이용하여 푸는법

n=int(input())
arr=[]

for i in range(n):
    arr.append(str(input()))

set_arr=set(arr)    
arr=list(set_arr)  

arr.sort()  
arr.sort(key=len)

for i in arr:
    print(i) 


''' sys와 strip함수를 통해 푸는법, sys.stdin.readline()은 '\n\'를 포함하는 입력이기 때문에 for문을 통해 연속적으로 입력을 받는 것은 오류를 초래한다.
따라서 strip함수를 이용해서 문자열 앞뒤를 제거해줘야한다. input보다 복잡하지만 처리속도가 매우 빠르다.

import sys

n=int(sys.stdin.readline())
arr=[]

for i in range(n):
    arr.append(str(sys.stdin.readline().strip()))   # strip을 하지 않으면 출력형식이 잘못된다고 뜬다, strip함수는 문자열 앞뒤를 제거한다.

set_arr=set(arr)    # set은 중복된 값을 제거한다. 하지만 다시 list타입으로 저장하지 않기 때문에 변수 선언 후
arr=list(set_arr)   # 다시 list타입으로 변환해준다.

arr.sort()  # 길이가 짧은 것부터가 1순위 조건이고 그다음은 길이가 같을경우 사전 순이므로 하위조건대로 먼저 정렬한다.
arr.sort(key=len)

for i in arr:
    print(i) 
'''