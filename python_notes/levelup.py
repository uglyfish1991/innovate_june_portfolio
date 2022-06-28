# print("this is level up")

# print(int(5.6))
# print(type(int("54")))

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

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")

    try:
        print(int(num1) + int(num2))
    except:
        print("Please use numbers only")
        print("try again")
        add_up()
add_up()

