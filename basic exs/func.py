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

3
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

5
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



























