'''
X,Y,W,S=map(int,input().split())    # X,Y는 좌표, W는 한블럭 갈 때 걸리는 시간, S는 대각선으로 갈 때 걸리는 시간
time=0

if(S>=2*W):
    time=X*W+Y*W
    print(time)
else:
    if(X>=Y):
        time=Y*S
        time+=(X-Y)*W
    else:
        time=X*S
        time+=(Y-X)*W

    print(time)

위와 같은 방법은 대각선으로 갔다가 대각선으로 돌아오는 방안을 구현 못함
따라서 여러 경우의 수를 변수에 담고 최솟값을 구해야함
'''
X,Y,W,S=map(int,input().split())    # X,Y는 좌표, W는 한블럭 갈 때 걸리는 시간, S는 대각선으로 갈 때 걸리는 시간

# 평행으로만 이동
move1=(X+Y)*W

# 대각선으로만 이동(X+Y가 짝수일 때)
if((X+Y)%2==0):
    move2=max(X,Y)*S
else:   # X+Y가 홀수일 때
    move2=(max(X,Y)-1)*S+W  # 딱 한번은 평행으로 이동해야 하기 때문에 -1을 한 후 W를 더해줌

# 대각선+평행이동
move3=(min(X,Y)*S)+((max(X,Y)-min(X,Y))*W)  # X,Y좌표중 최솟값만큼 대각선으로 이동하고 최댓값-최솟값만큼은 평행이동을 한다.

print(min(move1,move2,move3))
