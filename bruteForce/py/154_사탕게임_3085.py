import sys

def count(arr):
    n=len(arr)
    result=1

    for i in range(n):  # 가로 확인
        cnt=1
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]:
                # 이전과 색이 같다면 먹을 수 있는 사탕 수가 늘어나므로 cnt+=1
                cnt+=1
                result=max(cnt,result) # 가장 긴 줄을 골라야하므로 최댓값을 담는다
            else:
                # 다르면 1로 초기화
                cnt=1      
        cnt=1  
        for j in range(1,n):
            if arr[j][i]==arr[j-1][i]: # 세로 확인
                # 이전과 색이 같다면 먹을 수 있는 사탕 수가 늘어나므로 cnt+=1
                cnt+=1
                result=max(cnt,result) # 가장 긴 줄을 골라야하므로 최댓값을 담는다
            else:
                # 다르면 1로 초기화
                cnt=1
            
    return result

n=int(sys.stdin.readline())
b=[]

for i in range(n):
    b.append(list(sys.stdin.readline().rstrip()))

answer=0

for i in range(n):
    for j in range(n-1):
        b[i][j],b[i][j+1]=b[i][j+1],b[i][j] # 자리 바꾸기(가로)
        answer=max(answer,count(b)) # 자리를 바꿨으니 길이를 확인해주고 최댓값을 answer에 담는다.
        b[i][j],b[i][j+1]=b[i][j+1],b[i][j] # 다시 원상복구 시킨다.

for i in range(n-1):
    for j in range(n):
        b[i][j],b[i+1][j]=b[i+1][j],b[i][j] # 자리 바꾸기(세로)
        answer=max(answer,count(b)) # 자리를 바꿨으니 길이를 확인해주고 최댓값을 answer에 담는다.
        b[i][j],b[i+1][j]=b[i+1][j],b[i][j] # 다시 원상복구 시킨다.

print(answer)
        
