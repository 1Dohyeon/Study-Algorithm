N=int(input())
num=0
line=0

# 몇 번째 줄인지 구한다
while num<N:
    line+=1
    num+=line   # num은 그 라인에서 가장 큰 순서가 됨

gap=num-N   # 최대 순서와 입력 받은 순서의 차이

if line%2==0:   # 짝수 번째 줄일 때
    f1=line-gap # 분자
    f2=gap+1    # 분모
else:
    f1=gap+1
    f2=line-gap

print('%d/%d'%(f1,f2))



