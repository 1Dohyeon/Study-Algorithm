#d = [[0]*19 ]*19 
'''
Python에서는 * 연산자를 이용해 배열을 선언하게 되면, 얕은 복사(shallow copy)가 진행된다.
즉, 배열 내의 요소들이 같은 객체를 가리키게 되는 것이다.
따라서, 이 방식으로 2차원 배열을 선언하고 요소를 변경하게 되면 다른 요소들의 값도 같이 바뀌는 것이다.
'''

d = [[0 for j in range(20)] for i in range(20)] #0~19, 0~19 20개씩이다

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) : #(1,1)에서(19,19까지)
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()
