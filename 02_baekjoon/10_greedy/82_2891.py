N,S,R=map(int,input().split())
damaged = list(map(int, input().split())) # 카약이 손상된 팀 번호
onemore = list(map(int, input().split())) # 카약이 남는 팀 번호

result=S    # 출발할 수 없는 팀의 수

for i in range(S):
    for j in range(R):
        if((damaged[i]==onemore[j]) or abs(damaged[i]-onemore[j])==1):  #abs는 절대값을 의미
            result-=1
            del onemore[i]
            R-=1
            break

print(result)