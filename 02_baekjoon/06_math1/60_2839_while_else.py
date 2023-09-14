N=int(input())
count=0

while N>=0:
    if N%5==0:
        count+=N//5
        print(count)
        break

    N-=3
    count+=1

else:   # else 구문으로는 0으로 나누어 떨어지지 않을 시 -1을 출력하도록 한다.
    print(-1)

'''while else에서 else 뒤의 문장은 while의 조건이 거짓이 될 경우 실행된다. 즉 N<0 일 때 else 뒤의 문장이 실행된다.
하지만 N을 계속 줄여나가다가 0과 같아도 while은 계속 진행하게 되어있다. 하지만 0일때는 5로 나눌 경우 나머지가 0이기 때문에 if절로 들어가고 몫이 0이기에
0을 count에 더하고 break한다. if 절로 들어가지 않고(0이라는 수를 거치지 않고) 음수가 될경우 바로 else뒤 문장을 실행한다.'''