score = int(input())

if score>=90 and score<=100:
    print('A')
else:
    if score>=70 and score<=89:
        print('B')
    else:
        if score>=40 and score<=69:
            print('C')
        else:
            if score>=0 and score<=39:
                print('D')