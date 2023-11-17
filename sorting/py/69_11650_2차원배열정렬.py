n=int(input())
arr=[]

for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))   # 2차원 리스트에 변수 담기

arr.sort()  # 2차원 리스트도 sort를 이용해 정렬할 수 있다.

for i in range(n):
    print(arr[i][0],arr[i][1])  # 첫번째 배열을 기준으로 나눈것이 아닌 두번째 배열을 기준으로 2로 쪼갠거기 때문에 2번째 배열을 0,1로 고정시킨다.