import sys

cm=[]

for i in range(9):
    cm.append(int(sys.stdin.readline()))

for i in range(len(cm)-1):
    for j in range(i+1,len(cm)):
        a=cm[i] # cm[i]와[j]를 모두 0으로 만들고 합을 구할거기 때문에 원래 있던값을 저장해둔다
        b=cm[j]
        cm[i]=0
        cm[j]=0
        if sum(cm)==100:
            break
        else:
            cm[i]=a # 합이 100이 안되면 다시 원상복구 시켜주고 반복
            cm[j]=b

cm.remove(0)    # 합이 100이라 break되었다면 배열의 0을 모두 지워주고 정렬시킨다.
cm.remove(0)
cm.sort()

for r in cm:
    print(r)