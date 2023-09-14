V=int(input())
w=list(str(input()))

A=w.count('A') #w에서 A의 갯수를 세고 그 수를 변수 A에 저장
B=w.count('B')

if A > B:
    print('A')
elif A == B:
    print('Tie')
else:
    print('B')