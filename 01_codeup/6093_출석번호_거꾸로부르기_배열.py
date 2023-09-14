n = int(input())
arr = list(map(int,input().split())) #배열이 아니라 리스트임

for i in range(n-1,-1,-1): # n-1부터 -1+1번째까지 -1순으로
    print(arr[i],end=' ')

'''
n = int(input())
arr=[0]*n  ----------> 이런식으로 배열을 만들 수 있음(추천하지 않음)

for i in range(0,n):
    arr[i]=int(input())

for i in range(n-1,-1,-1): # n-1부터 -1+1번째까지 -1순으로
    print(arr[i],end=' ')
'''