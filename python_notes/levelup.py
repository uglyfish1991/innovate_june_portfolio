import random

print("this is level up")

print(int(5.6)) #even though this is a floating point, we're converting it into an int
print(type(int("54"))) #even though this is a string, we're converting it into an int
#print(int("hello")) <- this would cause us a fatal error 

# balance = 100

# deposit = int(input("how much do you want to deposit?"))

# balance +=deposit
# print(f"You have {balance}")

# print("What is your name?")
# name = input()

# if name:
#     print(f"Welcome {name} to Innovate!")
# else:
#     print("You did not submit a name")

# day="Monday"
# bank_hol = ""

# if day =="Saturday" or day=="Sunday" or bank_hol: 
#     print("Yay a day off")
# else:
#     print("Off to Innovate we go")

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")

#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use numbers only")
#         print("try again")
#         add_up()
# add_up()
# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True

# light_switch()
# light_switch()
# light_switch()
# light_switch()
# light_switch()
# light_switch()
#this is a list
# even_nums =[2,4,6,8,10]
# #it can be changed or mutated with methods
# #we can insert, remove, append, pop and more to change the properties of the list
# even_nums.append(12)
# even_nums.insert(0,0)
# print(even_nums)

# # this is a tuple, it is immutable -> it cannot be changed via methods
# odd_nums=(1,3,5,7,9)
# # odd_nums.append(11)this would not work on a tuple
# print(odd_nums)

#my list
fav_songs = [
    "The foundations of decay - my chemical romance",
    "Pandemonium - Killing Joke",
    "Jigsaw Falling into Place Radiohead",
    "Army of me _ Bjork"
]
#start:stop:step
# print(fav_songs[1]) #this is an index position - it is the start value
# print(fav_songs[1:2:1]) #this is actually what is happening - starting at one, stopping short of 2, and stepping by 1 at a time

# # make a string Variable

# # if it reads forwards the same as backwards
# # if it does say YESif it doesn't say no

# # print(fav_songs[::]) slices through the whole list, start to end, stepping by the default 1

# test = "TooT"

# if test == test[::-1]:
#     print(f"Yes! {test} is a palindrome")
# else:
#     print("It is not a palindrome")

# loop_run=True
# while loop_run==True:
#     print("This will run forver")
#     loop_run=False

# this is a while loop that compares a variable and runs under a condition
num=random.randint(1,50)

while num%2==0:
    print("We like even numbers! Another!")
    num=random.randint(1,50)
#if the number is odd, the while loop will never ever run
print("Oh no! An odd number!")
######################################################
while True:
    num=random.randint(1,50)
    print(num)
    if num%2==0:
        print("We like even numbers! Another!")
        continue
    else:
        print("An odd number!")
        break
#this while loop will always initialise. It might go straight to the else/break - but it will have started

