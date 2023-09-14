num=int(input())
range=1
room=1

if(num==1):
    print(room)
else:
    while True:
        range+=room*6
        room+=1
        if(range>=num):
            break

    print(room)

