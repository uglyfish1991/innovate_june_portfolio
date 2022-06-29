
def is_answer_num():
    answer = input("Please type in a number")

    try:
        print(int(answer))
        print(type(int(answer)))
    except:
        print("try again")
        is_answer_num()

is_answer_num()

