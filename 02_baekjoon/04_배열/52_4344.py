case=int(input())

for i in range(case):
    n=list(map(int,input().split()))
    avg=sum(n[1:])/n[0]
    count=0

    for j in range(1,n[0]+1):   # range(1,n[0]+1)말고 n[1:]이라고 바꾼 뒤 if문에 n[j]를 j라고만 둬도 된다.
        if(n[j]>avg):
            count+=1

    result=count/n[0]*100
    
    print(f'{result:.3f}%')
   
