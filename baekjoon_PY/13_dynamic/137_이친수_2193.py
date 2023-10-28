import sys

n=int(sys.stdin.readline())
d=[0,1,1]

for i in range(3,91):
    d.append(d[i-1]+d[i-2]) # 마지막 숫자가 0일 경우 그 전 숫자는 1과 0 두개가 될 수 있다. 결국 바로 전 d[i-1]의 경우의 수와
                            # 같다는 의미이다. 마지막 숫자가 1인 경우는 전의 숫자는 0밖에 되지 않는다. 전의 숫자가 0인 경우의
                            # 수는 앞에서 구한 것처럼 d[i-1]이기 때문에 d[i-1-1]인 d[i-2]를 갖게 되고 이 두 식을 더한 값이
                            # d[i]가 된다.  

print(d[n])


'''
2차원 배열 풀이
n=int(sys.stdin.readline())
d=[[0 for i in range(2)] for j in range(91)]

for i in range(1,91):
    d[i]=[0,1]

d[1][0]=0
d[1][1]=1

for i in range(2,91):
    d[i][1]=d[i-1][0]
    d[i][0]=d[i-1][0]+d[i-1][1]

print(sum(d[n]))
'''


