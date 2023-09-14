N=int(input())
arr=[]

for i in range(N):
    a,b=map(int,input().split())
    rev_arr=[b,a]   # a,b를 바꿔준다, y좌표가 0번째 배열에 담긴다.
    arr.append(rev_arr) # 바꾼 값을 arr리스트에 담는다

arr.sort()  # arr을 정렬한다

for i in range(N):
    print(arr[i][1],arr[i][0])