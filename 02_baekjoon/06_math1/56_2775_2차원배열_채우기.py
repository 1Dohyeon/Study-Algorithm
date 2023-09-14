case=int(input())

for i in range(case):
    k=int(input())  # 층(1<=k<=14)
    n=int(input())  # 호(1<=n<=14)
    room=[[0 for j in range(0,14)] for i in range(0,15)]  #0~14층, 1~14호->배열은 0~13번째
    
    # 반복문만 이용
    for x in range(15):
        room[x][0]=1

    for y in range(14):
        room[0][y]=y+1

    for x in range(1,15):
        for y in range(1,14):
            room[x][y]=sum(room[x-1][:y+1])

    print(room[k][n-1])

    # 조건문을 이용
    '''for x in range(15): #층
        for y in range(14): #호
            if x==0: 
                room[x][y]=y+1
            else:
                if y==0:
                    room[x][y]=1
                else:
                    room[x][y]=sum(room[x-1][:y+1])'''

