a,b,c=input().split()
'''(a if a>b else b) if ((a if a>b else b)>c) else c는
a가 b보다 크다면 a를 아니면 b를 출력한 후 그 값과 c를 비교하여
c가 더 크면 c를 아니면 처음 출력한 수를 최종 출력한다는 뜻이다'''

#즉 if 앞과 else의 뒤를 바꾸면 가장 작은 수를 출력한다.

print(c if ((b if a>b else a)>c) else (b if a>b else a))