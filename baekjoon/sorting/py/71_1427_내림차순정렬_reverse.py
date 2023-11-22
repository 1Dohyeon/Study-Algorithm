n=list(map(int,str(input())))   # 입력값을 받을 때부터 모든 수를 슬라이싱하여 리스트로 담는법, 예를 들면 1234라는 수를 받으면 [1, 2, 3, 4]로 받은 것이다
n.sort(reverse=True)    # 내림차순 정렬법

for i in n:
    print(i,end='') # end=''를 이용하면 한 줄씩 출력되어야 할 i를 띄어쓰기 없이 출력한다.
