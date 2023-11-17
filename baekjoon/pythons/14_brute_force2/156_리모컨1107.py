import sys
input=sys.stdin.readline

cha=int(input())
m=int(input())
dw=list(map(int,input().split()))

cnt=abs(100-cha)    # + or - 로만 이동할 경우를 기본값(최댓값) 설정

for i in range(1000001):    # 문제 범위의 채널만큼 전부 탐색
    i=str(i)

    for j in range(len(i)): # 채널 i의 길이만큼 또 탐색
        if int(i[j]) in dw: # i[j]중 부러진 번호가 있을 경우
            break   # 반복문을 나감
        elif j==len(i)-1:   # j가 i의 마지막 숫자일 경우
            cnt=min(cnt,abs(int(i)-cha)+len(i)) # 탐색하면서 구한 cnt 와 채널의 차의 절댓값 - len(i) 중 최솟값을 구한다. 

# 예를 들어 500000번을 틀고 싶은데 0 2 3 4 6 7 8 9 번이 고장났을 경우
# 반복문이 탐색을 시작할 때 511111일 때 break되지 않고 최솟값을 찾는다.

print(cnt)

