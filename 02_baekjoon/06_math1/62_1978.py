# 소수찾기

n=int(input())
num=list(map(int,input().split()))
count=0

for i in num:
    k=0
    if i==1:
        continue
    else: 
        for j in range(2,i):
            if i%j==0:
                k+=1
        if k==0:
            count+=1

print(count)

'''자기 자신과 1로만 나뉘는 수를 소수라고 한다. 즉 2와 자기 자신보다 1 작은 수로 계속 나눈 다음 나머지가 0이 나온다면 소수가 아니므로 k에 1을 더하든
빼주든 하여 k=0이 아니게 만든다. 그리고 k가 0이라면 소수란 의미이므로 count 해준다.
'''




