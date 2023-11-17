while True:
    n=int(input())
    if(n==-1):
        break
    k=[]
    for i in range(1, n): #자기 자신은 안더하기 때문에 n+1할 필요 없음
        if(n%i==0):
            k.append(i)

    if (sum(k)==n):
        print(n,"=",end=" ") #end를 붙여줌으로서 뒤에 출력은 \n이 아닌 띄어쓰기 후 출력
        print(*k,sep=" + ") #k앞에 *을 붙여주지 않으면 sep가 실행되지 않음
    else:
        print(n, "is NOT perfect.")