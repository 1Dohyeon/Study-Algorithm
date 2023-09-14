doc=input()
word=input()
count=0
n=0

while(n<=len(doc)): # 왜 len(doc)-len(word)라고 해도 맞는지 모르겠음;;
    if(doc[n:n+len(word)]==word):   #doc[n]이라는 배열은 n번째에서 len(word)만큼의 길이의 배열을 갖는다는 의미 (n, n+len(word)+1)
        count+=1
        n+=len(word)
    else:
        n+=1

print(count)
