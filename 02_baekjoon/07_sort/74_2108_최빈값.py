import sys
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(n):
    num.append(int(input()))

# 산술평균
print(round(sum(num)/len(num))) # 소수점 첫재짜리에서 반올림하는 경우 round를 쓰면 깔끔하다.

# 중앙값
num.sort()
print(num[(n-1)//2])

# 최빈값 
## 최빈값 리스트 초기화값 생성
result=[num[0]]
## 현재 숫자 개수를 세는 변수
cnt=1
## 최빈값에 해당하는 개수 변수
cnt_max=0
# 이전 숫자에 해당하는 변수
last=num[0]

# 숫자를 하나씩 받으면서
for i in num[1:]:
	# 이전 숫자와 현재 숫자가 불일치하고
    if i!=last:
        ## 특정 수의 개수가 현재 최빈값 개수보다 많다면
        if cnt>cnt_max:
            ## 최빈값 리스트 초기화
            result=[]
            ## 최빈값 리스트에 추가
            result.append(last)
            cnt_max=cnt
        ## 특정 수의 개수가 현재 최빈값 개수와 같다면 최빈값 추가
        elif cnt==cnt_max and last not in result:
            result.append(last)
        cnt=1
    ## 중복된 수가 존재한다면 cnt 개수 추가
    else: 
        cnt+=1
    last=i

## 마지막 수 계산
if cnt>cnt_max:
    result=[last]
elif cnt==cnt_max and last not in result:
    result.append(last)

## 최빈값이 1개라면 단일값 출력
if len(result)==1:
    print(result[0])
## 최빈값이 여러개라면 두 번째로 작은 값 출력
else:
    print(result[1])    # 이미 sort()함수로 올림차순 정렬을 했기 때문에 result에 담기는 값도 자동으로
                        # 올림차순이기 때문에 두번 째로 작은 값은 result[1]로 출력이 가능하다.

# 범위
print(max(num)-min(num))
