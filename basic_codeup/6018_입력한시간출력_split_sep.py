a, b = input().split(":") #input().split(":") 입력인자를 받는 input()함수에 .split(":")을 사용하여 :으로  이들을 구별하게 해두었다.
#즉 x:y로 입력하면 a=x, y=b가된다.
print(a,b,sep=":") #print(a,b)는 a b로 띄어쓰기를 두고 출력하지만, sep=":"을 이용하여 a:b로 각 인자를 :로 구별해서 출력한다.