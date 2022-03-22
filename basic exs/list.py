# 1
print("i love python"*5)

# 2
numbers= [1,2,3,4,5,6,7,8,9,10]
print(numbers)

# 3
names =["rivka","simha","salmon","eli","yonatan","miki","betty","aviva","oshrat","yemikir"]
print(names)
x=sorted(names)
print(x)

# # 4
x = [10,45,88,78,64,98,23,56,44,12,3,]
print(sum(x))

for j in x:
    print(j/11)

for i in x:
    if i > 10:
        print("bigger then 10:" , i)

for i in x:
    if i < 10:
        print("smaller then 10:" , i)

print(max(x))

for i in x:
    if i % 2 == 0:
        print(i)

for i in x:
    if i % 3 == 0:
        print(i)

# 5
data =[1,2,8,9,6,20,6,18,28,29,30]
def consecutives(data):
    start = 0
    i = start
    while i < len(data) - 1:
        if data[i] + 1 == data[i + 1]:
            i += 1
        else:
            yield(start, i - start + 1)
            start = i + 1
            i = start
    yield(start, i- start + 1)

for seq in consecutives(data):
    print(seq)

data.insert(0,3)
print(data)

num = int(input("please enter a number: "))
data.insert(1,num)
print(data)

x = data[1]+data[2]
data.insert(3,x)
print(data)

x= data[0]*data[1]*data[2]
data.insert(4,x)
print(data)

print(data)

# grade
l1=[]
l2=[]
for i in range(5):
    l1.append(int(input("please enter your grade:")))
    l2.append(int(input("please enter your grade:")))

for i in l1:
    for j in l2:
        if i == j:
            print(i , "grade in both")

# shvilisrael
shvil = []
sum = 0
for i in range(3):
    name = input("enter a name: ")
    dist = int(input("enter a length: "))
    shvil.append([dist])

    if dist > 10:
        sum += dist
        print(dist)

print("sum of shvil : ", sum)

# 8
sum=0
for i in range(5):
    fname=input("enter a last name : ")
    kids=int(input("enter number of kids : "))
    print(fname, kids)
    if kids>3:
        print("DISCOUNT")
    sum += kids

print(sum)

# 9
count = 0
for i in range(3):
    name = input("please enter your name : ")
    year = int(input("please enter your birth year : "))
    blood = input("please enter your blood type a/o/b/ab: ")
    if blood == 'o':
       count = count+1

    print(name, year, blood)
print(count)

# 10
word = input("enter some word :")
word_list = list(word)
print(word_list)
print(len(word))


