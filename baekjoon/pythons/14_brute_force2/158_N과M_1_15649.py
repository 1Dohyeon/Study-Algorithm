'''
import itertools    # Python에서 손쉽게 순열, 조합 등을 구할 수 있는 함수를 제공

n,m=map(int, input().split())
nums=[i for i in range(1, n+1)]

arr=itertools.permutations(nums,m)  # 순열 함수

for i in arr:
    for j in i:
        print(j,end=' ')
    print()
'''
# DFS의 일종인 백트래킹(재귀함수)

n,m=map(int, input().split())
num=[]

def dfs():
    if len(num)==m:
        print(' '.join(map(str,num)))   # 리스트의 원소의 갯수가 m이면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
        return 

    for i in range(1,n+1):  # 1부터 n까지 모든 수를 탐색
        if i not in num:    # 중복여부를 확인하여 리스트에 i가 없을 경우 i를 push
            num.append(i)
            dfs()           # i가 push될 때마다 자기 자신의 함수를 실행하여 위 if문을 실행하고 len(num)=m일 때 리스트의 원소들을 문자열로 ' '띄어쓰기와 같이 
            num.pop()       # 출력하고 pop를 통해 리스트의 마지막 원소를 삭제한다.(재귀함수)
                            # ex)
                            # 만약 n=4, m=2라면 
                            # num : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
                            # 출력   pop(2)  출력   pop(3)  출력

dfs()

