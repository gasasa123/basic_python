# # 1
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#
# # 2
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
#
# # 3
# import math
# def pi():
#     print(math.pi)
#     return
# radius = int(input("please enter radius of a circle : "))
# print(pi())

# # 4
# fname = input("please enter your first name : ")
# lname = input(("please enter your last name : "))
# print(lname,"",fname)

# # 5
# numbers = []
# num3 = ()
# for i in range(10):
#     num = int(input("please enter number : "))
#     numbers.append(num)
# print(numbers)

# # 6
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])
# print(color_list[-1])

# # 7
# exam_st_date = (11, 12, 2014)
# print("The examination will start from : %i / %i / %i"%exam_st_date)

# # 8
# date1 = (2014, 7, 5)
# date2 = (2014, 7, 25)
# print(date1[-1]-date2[-1],"days")

# # 9
# num = int(input("please enter a number : "))
# if num > 17 :
#     print((num - 17)*2)
# else:
#     print(num - 17)

# # 10
# num = int(input("please enter a number : "))
# if num % 2 == 0:
#     print("the number it even")
# elif num % 2 != 0:
#     print("the number is odd")

# # 11
# num = int(input("please enter a number : "))
# for i in range (num):
#     if i % 2 ==0:
#         print(i)

# # 12
# x=0
# num = int(input("please enter a number : "))
# while x < num:
#     if num % 2 == 0:
#         x += 2
#         print(x)

# 13 dictionary
# student = {"name":"eliya",
#            "course":"python",
#            "age":36
#            }
# print(student.items())
#
# for i in student.values():
#     print(i)

# for x,y in student.items():
#     print(x,y)

# 14
# student = {"name":"rivka",
#            "age": 28,
#            "city" : "ramle",
#            "school" : "tech career",
#             "course":"python"
# }
# print(student.keys())
# print(student.values())
# print(student["age"])
# for x,y in student.items():
#     print(x,y)
# student.pop("city")
# print(student)

# # 15
# name = ["rivka" , "aviva" ,"daniel" , "eli" , "yealem"]
# for x in name:
#     print(name.index(x),x)

# # 16
# def looplist(x):
#     for i in range(x):
#         yield i
#
# print(list(looplist(5)))

# # 17
# def name (x):
#     print("hello" , x)
#
# name("rivka")

# # 18
# def multi (x,y):
#     a =x*y
#     print(a)
#
# multi(10,6)
#
# def looplist(x):
#     for i in range(x):
#         yield i
#
# print(list(looplist(9)))

# # 19
# x = 100
# def func():
#     global x
#     x = 500
#
# func()
# print(x)

# # 20
# def three (x,y,z):
#     print(x,y,z)
#
# three(10,66,28)

# # 21
# def oddoreven (num):
#     if num % 2 ==0:
#         print("even number")
#     if num % 2 != 0:
#         print("odd number")
#
# num = int(input("enter a number : "))
# oddoreven(num)

# # 22
# def get_numbers():
#     my_numbers = []
#     for i in range(1,6):
#         num = int(input("please enter a number :"))
#         my_numbers.append(num)
#     return my_numbers
















