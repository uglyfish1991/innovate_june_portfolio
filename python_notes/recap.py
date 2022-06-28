# import random
# # # this is how to show information

# # print("this is my file")

# # greeting = "Hello everyone!"

# # print(greeting)

# # print("This is a string for displaying characters")
# # print("1234") #this is a string
# # print(1234+1) #this is an integer/whole number
# # print(12.34) #this is a float
# # print(True) #one of the booolean data values
# # print(False) #one of the booleans
# # print(None) #none - blank/null data

# # print(len(greeting))

# # print(greeting[-1])

# # print(greeting.upper())
# # print(greeting)

# # print("HELLO".lower())
# # print("hello EVERYONE. THIS is innovate".capitalize())
# # print("This quick brown fox fox fox".count("Fox"))
# # print("The quick brown fox".find("T"))
# # print("The quick brown fox".replace("fox","frog"))
# # print(("The quick brown fox").strip("quick"))

# # print(random.random())

# # print(random.uniform(1,10))

# # print(random.randint(1,10))

# my_name="Katy"
# my_age=30
# student=False

# # print(my_name,my_age,student)

# # print("Hello my name is", my_name)
# # print("I am", my_age)

# # print("Hello my name is " + my_name)
# # print("I am" + my_age)

# #.format() method - used to be best practise.
# # uses {} as placeholders and data is filled in their place based on order of args. in method
# print("Hello my name is {} and I am {} years old".format(my_name,my_age))
# # f string, new best practise
# print(f"Hello my name is {my_name} and I am {my_age} years old")

# print(1+2)
# print(3-2)
# print(3*3)
# print(3**3)
# print(6/2)
# print(16%3)

# balance=10
# print(balance)
# amount=200

# balance=amount+balance
# balance +=amount
# print(balance)

# answer=input("What is your name? \n")
# print(answer)

# music = "Classical"

# if music == "classical":
#     print("Oh no it's classical")
# elif music == "no music":
#     print("Put the radio on")
# elif music =="my chemical romance":
#     print("Katy, stop crying")
# else:
#     print("turn it up")

# print("That was an if statement")

# print(10%3==0)

# num=10
# num2=20

# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print("Both are equal")

# place ="MCR"
# weather="Rainy"

# if place=="MCR" and weather=="Sunny":
#     print("Check again")
# elif place=="MCR" and weather=="Cloudy":
#     print("What is isn't raining?")
# else:
#     print("obvs")

# day = "Monday"
# bank_hol = False

# if day=="Saturday" or day=="Sunday" or bank_hol:
#     print("A day off")
# else:
#     print("Off to Innovate we go")

# def light_switch():
#     print("Switching the lights")

# light_switch()
# light_switch()
# light_switch()

# def cash_with(amount,accnum):
#     print(f"From your account {accnum} you have withdrawn {amount}")

# cash_with(300,12345678)
# cash_with(100,12309876545678)
# cash_with(334567,134567)

fav_songs = [
    "The foundations of decay - my chemical romance",
    "Pandemonium - Killing Joke",
    "Jigsaw Falling into Place Radiohead"
]

print(fav_songs)

fav_songs[1] = "Adam's Song- Blink 182"

print(fav_songs)

print(len(fav_songs))

fav_songs.append("Army of Me - Bjork")

print(fav_songs)

fav_songs.pop(2)

print(fav_songs)