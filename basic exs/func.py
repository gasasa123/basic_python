# 1
def plus (x,y):
   print(x+y)

print(plus(15,25))

# 2
def rivka (x,y):
   z =(x+y)
   return z

# call function
s =rivka(5,10)
print(s)

# 3
def notgetandnotreternfunc():
    print("hi from ... ")

def getandnotretern(x):
    print(x)

def notgetandreterunfunc():
    return "hi rivka ,,,, "

def getandreturnfunc(x, y):
    return x * y

notgetandnotreternfunc()
getandnotretern(8)
v = notgetandreterunfunc()
print(v)
a=getandreturnfunc(7,3)
print(a)

# 4
def countnumbers (ls):
    newls=[0,0,0,0,0,0,0,0,0,0]
    for i in ls:
        newls[i] += 1
    return newls

ls = [1,1,2,7,3,5,8,9]

newls = countnumbers(ls)
print(newls)

# 5
def avg ():
    sun = 0
    count = 0
    num = input("enter a number : ")
    while num != q:
        count +=1
        sum = int(num)
        num = input("enter a number : ")

    print(sun/count)
avg()


# 6
def palindrom(x):
start = 0
end = len(st)-1
for i in range(len(st)//2):
    if str(start) != st(end):
        print("not palindrom")
        return
    else:
        start = 1
        end = 1
print("palindrom")
palindrom("abba")

# 7
def minute(x):
    print(x / 60)
min = int(input("please enter a minutes :"))
minute(min)

# 8
def posorneg(ls):
    for i in ls:
        if i > 0:
            print("Positive number")
        if i == float or i < 0:
            print("negative number")

ls = [8,9,-1,5,16.3,28,77,98]
posorneg(ls)

# 9
def evenorodd (x):
    if x % 2 == 0 :
        print("0")
    else:
        print("1")
num = int(input("enter a number: "))
evenorodd(num)

# 10
num = str(input("enter a number whit 6 digit : "))
even = 0
odd = 0
for i in (num):
    a=int(i)
    if a%2==0:
        even+=1
    else:
        odd+=1
print(even,"even number")
print(odd,"odd number ")

# 11
def avg (x,y,z):
    a = (x+y+z)//3
    print(a)

x=int(input("please enter a number :"))
y=int(input("please enter a number :"))
z=int(input("please enter a number :"))
avg(x,y,z)

# 12
def lenofnum(x):
    print(len(x))

num = str(input("enter a number:"))
lenofnum(num)

# 13

def Odef(x):
    x = int(input(" enter your change :"))

    Esrem_Shekel = int(x / 20)
    Eser_Shekel = int((x % 20) / 10)
    Hamesh_Shekel = int(((x % 20) % 10) / 5)
    Shekel = int((((x % 20) % 10) % 5) / 1)

    print("number of 20 : ", Esrem_Shekel)
    print("number of 10 : ", Eser_Shekel)
    print("number of 5 : ", Hamesh_Shekel)
    print("number of 1 : ", Shekel)

# 14
def hezka (x,y):
    s = x**y
    print(s)

hezka(7,3)

# 15
def discount (x):
     a = (x*0.30)
     x=x-a
     print(x)

def price(x):
    if x > 1000:
        discount(x)
    else:
        b = (x*0.10)
        x=x-b
        print(x)

x = int(input("enter a price : "))
price(x)

# 16
import math
def hezka (x,y):
    s = x**y
    print(s)

x = int(input("enter first number : "))
y = int(input("enter second  number : "))
select = input("a - biggest devider \nb - smallest divider \nc - result of pow(a,b) \nd - result of sqrt(a)-sqrt(b) \nc - exit \n ")
if select == 'a' :
    print(math.gcd(x, y))
if select == 'b' :
    for i in range(2, x,y + 1):
        if (x,y % i == 0):
            print("The smallest divisor is:", i)
            break
if select == 'c':
    hezka(x,y)
if select == 'd':
    a = math.sqrt(x)
    b = math.sqrt(y)
    print(a-b)
if select == 'e':
    print("done !")

# 17
def specialprint():
    print("Give the customer a number", num, "special treatment")
def conditionstostore():
    if value > 8000 or pay == 'yes' or seniority > 6:
        specialprint()
    elif value > 8000 or pay == 'yes' or seniority < 6:
        specialprint()
    elif value > 8000 or pay == 'no' or seniority > 6:
        specialprint()
    elif value < 8000 or pay == 'yes' or seniority > 6:
        specialprint()
    elif value < 8000 or pay == 'yes' or seniority < 6:
        specialprint()
    else:
        print("custumer a number", num, "Not meeting the conditions")

num = int(input("enter your costumer number :"))
value = int(input("enter commodity value in year :"))
pay = input("Pay on time\n1 = yes , 0 = no :")
seniority = int(input("enter Years of store seniority :"))
conditionstostore()









