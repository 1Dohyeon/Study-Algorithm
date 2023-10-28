n=9
num=[(int(input())) for i in range(n)]  # for문을 이용하여 배열 선언

max_num=num[0]
k=1

for i in range(n):
    if max_num<num[i]:
        max_num=num[i]
        k=i+1
    
print(max_num,k,sep='\n')   # max_num과 k를 한줄 띄워서 출력한다.

