# 그릇의 높이는 10cm, 틈 5cm 따라서 두개를 포개면 
# 5cm만 증가하여 15cm 서로 반대로 쌓으면 
# 원래 높이 그대로 20cm가 된다

dish=list(str(input()))
h=0

for i in range(len(dish)):
    if(i==0):
        h+=10
    elif(dish[i]==dish[i-1]):
        h+=5
    elif(dish[i]!=dish[i-1]):
        h+=10

print(h)