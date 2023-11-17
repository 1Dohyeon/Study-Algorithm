T=int(input())

for i in range(T):
    H,W,N=map(int,input().split())  # 호텔의 층 수, 방 수, 손님 순서
    w=N//H+1
    h=N%H
    if N%H==0:
        h=H
        w=N//H
    
    print(h*100+w)
    
