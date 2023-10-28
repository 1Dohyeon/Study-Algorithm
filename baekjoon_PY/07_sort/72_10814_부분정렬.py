N=int(input())
p=[]

for i in range(N):
    age,name=map(str,input().split())
    age=int(age)
    p.append((age,name))    # 2차원 배열로 만들어서 푼다. 

p.sort(key=lambda p:p[0])  # (age, name)에서 age만 비교 후 정렬

'''
p.sort(key=lambda p:p[0])의 의미

sort함수에서 lambda를 통해 p의 0번째 배열만 정렬한다는 의미이다.
즉 작은 수가 앞으로 오게 되면서 뒤에 name까지 같이 앞으로 오게 되지만, 
age가 같을경우 뒤에 name을 비교하지 않고 그대로 다음절을 실행한다.
'''

for i in range(N):
    print(p[i][0],p[i][1])

''' 나이가 한자리수일 경우 문자열 맨 앞자리까지 비교값으로 들어오기 때문에 틀린 답이다
for i in range(N):
    p.append(input())

p.sort(key=lambda p:p[:3])  #입력값 앞 세자리만 비교해서 정렬

for i in p:
    print(i)
'''