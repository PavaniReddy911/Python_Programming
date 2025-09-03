def check(a):
    if a%2==0:
        print("A is even")
    else:
        print("A is odd")
check(23)


def num(a):
    if a>0:
        print("Positive")
    else:
        print("Negative")
num(-24)


def div(a):
    if a%5==0 and a%11==0:
        print("YES")
    else:
        print("NO")
div(55)
num(45)

def year(a):
    if a%4==0:
        print("Leap year")
    else:
        print("Not leap year")
year(100)


def alpha(a):
    arr=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    if a in arr:
        print("Alphabet")
    else:
        print("Not an alphabet")
alpha(a)


def acheck(a):
    vc=input("Enter alphabet")
    ar1=[a,e,i,o,u]
    if vc in ar1:
        print("vowel")
    else:
        print("consonent")
check(e)