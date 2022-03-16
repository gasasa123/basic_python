# parking.
hours = int(input("How long have you been parked?"))
if hours <= 3:
    print(hours*20)
elif hours >3 and hours <5:
    print(hours*15)

elif hours >5 and hours <24:
    print(hours*10)
else:
    print(hours*5)

# 2
a = int(input("please enter number1:"))
b = int(input("please enter number2:"))
if a>b:
    print("number1 bigger then number2")
    if b>a:
        print("number2 bigger then number1")
else:
    print("it even")

# 3
a = int(input("please enter number1:"))
b = int(input("please enter number2:"))
if a/b:
    print("The numbers are divided into each other")
    if (a % 2 == 0) and (b % 2 == 0):
        print("even number")

# 4
name = input("please enter your name:")
address = input("enter your address:")
school = input("please enter your school:")
age = input("please enter your age:")

name1 = input("please enter your name:")
address1 = input("enter your address:")
school1 = input("please enter your school:")
age1 = input("please enter your age:")

name2 = input("please enter your name:")
address2 = input("enter your address:")
school2 = input("please enter your school:")
age2 = input("please enter your age:")
if age and age1 > age2:
    print(name2,address2,school2,age2)
elif age and age2 > age1:
    print(name1, address1, school1, age1)
elif  age1 and age2 > age:
    print(name, address, school, age)

# 5
name = input("enter name of class:")
num = input("enter number of students:")
name1 = input("enter name of class:")
num1 = input("enter number of students:")
name2 = input("enter name of class:")
num2 = input("enter number of students:")
if num and num1 < num2:
    print(name2,num2)
elif num and num2 < num1:
    print(name1,num1)
elif num1 and num2 < num:
    print(name,num)

# 6
grade1 = int(input("enter your grade1:"))
grade2 = int(input("enter your grade2:"))
grade3 = int(input("enter your grade3:"))
grade4 = int(input("enter your grade4:"))
big=0
small=100
if grade1>grade4 and grade1>grade2 and grade1>grade3:
   big=grade1
elif grade2>grade1 and grade2>grade3 and grade2>grade4:
    bid=grade2
elif grade3>grade1 and grade3>grade2 and grade3>grade4:
    big=grade3
elif grade4>grade1 and grade4>grade2 and grade4>grade3:
    big=grade4

if grade1<grade4 and grade1<grade2 and grade1<grade3:
   small=grade1
elif grade2<grade1 and grade2<grade3 and grade2<grade4:
    small=grade2
elif grade3<grade1 and grade3<grade2 and grade3<grade4:
    small=grade3
elif grade4<grade1 and grade4<grade2 and grade4<grade3:
    small=grade4
print("the big number is",big)
print("the small number is",small)
print("the avg is:",(grade1+grade2+grade3+grade4)/4)

# 7
age = int(input("enter your age:"))
if age > 20 and age <= 40 or age > 30 and age <= 50 :
    height = int(input("enter yor height:"))
    if height > 180:
        print("You got a job")
else:
    print("You didn't get the job")

# 8
num = int(input("enter numbers between 1 - 10:"))
if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num == 6:
    print("six")
elif num == 7:
    print("seven")
elif num == 8:
    print("eight")
elif num == 9:
    print("nine")
elif num == 10:
    print("ten")
else:
    print("the number not between 1-10")


# 9
age = int(input("enter שge of the child:"))
if age > 7:
    print("go left")
elif age < 7:
    print("go right")

# 10
age = int(input("enter שge of the child:"))
if age > 7:
    print("go left")
else:
    print("go right")

# 11
dishes = int(input("How many dishes would you like?"))
if dishes == 1:
    print("15 shekels")
elif dishes == 2:
    print("25 shekels")
elif dishes ==3:
    print("30 shekels")
else:
    print("we sale until 3 dishes !")

# 12
print(3,11,7)
num = int(input("enter the largest number:"))
if num == 11:
    print("Bravo")
else:
    print("Try again")

# 13
num=int(input("enter integer number , onr digit number:"))
if num<10 and num>0 :
    if num%2==0 or num%3==0:
         print("all condition are heppen")
else:
    print("not one digit number")

# 14
age = int(input("enter your age:"))
if age >=0 and age<=120:
    print("Reasonable age")
else:
    print("not reasonable age")

# 15
num1=int(input("enter number:"))
num2=int(input("enter number:"))
if num1-num2==1 or num2*num1==1:
    print("Consecutive numbers")
else:
    print("not Consecutive numbers")

# 16
angle = int(input("please enter angle:"))
if angle >0 and angle<=89:
    print("acute angle")
elif angle>91 and angle<=180:
      print("obtuse angle")

# 17
experience = int(input("enter your years of experience:"))
if experience>=3:
    age=int(input("enter your age:"))
    if age>=25 and age<=40:
        print("you got a job")
else:
    print("sorry,you don't exceed the conditions")

# 18
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if b<a<c :
    print("in between")
else:
    print("not between")