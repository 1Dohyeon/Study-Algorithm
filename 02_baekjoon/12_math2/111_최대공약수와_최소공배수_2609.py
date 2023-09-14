# 유클리드 호제법

'''최대공약수는 gcd라고 부르며 두 수 a,b가 있을 때, a를 b로 나눈 나머지를 r이라고 했을 때 gcd(a,b)=gcd(b,r)이다.
r=0이 될 때, 그 때의 b가 최대 공약수이다.

ex) a=24,b=16일 때 r=24%16=8이 되고 gcd(a,b)=gcd(b,r)이기 때문에 24와 16의 최대공약수는 16과 8의 최대공약수와 같고 
여기서 다시 r=16%8=0이 되고, 이때의 b는 8이므로 최대공약수는 8이라는 성질을 이용한다.  

위와 같은 방법을 보면 계속 반복이다. 즉 반복문으로 나타낼 수 있다.

def gcd(a,b):   b가 0이 되면 반복이 멈추고 그때의 a(전 b)가 답이므로 return, 시간복잡도는 logN이다.
    while b!=0:
        r=a%b
        a=b
        b=r
    return a 

최소공배수는 lcm이라고 부르며 두 수 a,b가 있고 a,b의 최대공약수를 g라고 했을 때 lcm=g*(a/g)*(b/g)=(a*b)/g이다.
    ''' 

a,b=map(int,input().split())
x,y=a,b
while y!=0:
    r=x%y
    x=y
    y=r

print(x)    # 최대공약수

l=(a*b)/x
print(int(l))   # 최소공배수