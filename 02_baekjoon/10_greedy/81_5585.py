price=int(input())  #1~1000
change=1000-price   #거스름돈
coins=[500,100,50,10,5,1]   #거슬러질 동전, 큰 액수부터 거슬러줘야해서 내림차순으로 정리

sum=0   #거슬러 받아야할 동전의 갯수

for i in coins: #coins라는 배열에서 반복, i는 무조건 1부터 시작하지 않음, 이와 같은 경우는 500부터 100,50, ... , 1까지 내려가면서 진행
    sum+=change//i   
    change%=i

print(sum)