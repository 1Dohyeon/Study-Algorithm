n,m=map(int, input().split())
num=[]

def dfs(s):
    if len(num)==m:
        print(' '.join(map(str,num)))  
        return 

    for i in range(s,n+1):  
        if i not in num:   
            num.append(i)
            dfs(i+1)    # i를 이용하여 자신의 다음 숫자를 불러 중복을 없앤다.          
            num.pop()    

dfs(1)
# txt파일에 임의의 n,m을 주어 함수 진행을 살펴봄