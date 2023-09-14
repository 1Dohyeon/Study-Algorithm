a,b,c=map(int,input().split())

if(b>=c):   # 가변 비용이 노트북의 가격보다 같거나 크면 이익을 볼 수 없으므로 -1을 출력하여 오류임을 표시한다.
    print(-1)
else: 
    print(int(a/(c-b)+1))
    

    
