n=int(input())
count=0
k=n

while True:

    n1=k//10 # k의 10의자릿수   
    n2=k%10 #k의 1의자릿수
    n3=n1+n2    
    n4=n3%10    #합의 1의자릿수    
    n5=n2*10+n4 #다음 수열의 수
    count+=1    
    k=n5    

    if k==n:
        break

print(count)
