n,m=map(int, input().split())
num=[]

def dfs():
    if len(num)==m:
        print(' '.join(map(str,num)))   
        return 

    for i in range(1,n+1):   # for문을 통해 숫자를 늘려가며 배열에 담기 때문에 sort로 정렬할 필요가 없다.
        num.append(i)
        dfs()           
        num.pop()       

dfs()