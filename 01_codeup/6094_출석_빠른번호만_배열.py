n = int(input())
arr = input().split()

for i in range(n) :
  arr[i] = int(arr[i])
min = arr[0]
for i in range(0, n):
  if arr[i] < min :
    min = arr[i]
print(min)

'''
n = int(input())
arr=[0]*n  ----------> 이런식으로 배열을 만들 수 있음

for i in range(0,n):
    arr[i]=int(input())

min = arr[0]
for i in range(0, n) :
  if arr[i] < min :
    min = arr[i]
print(min)
'''

