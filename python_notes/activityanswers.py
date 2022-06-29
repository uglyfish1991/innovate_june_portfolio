# test_string = "Welcome to Code Nations"



def odd_even_checker(test_string): #passing the string through as a parameter/argument so the function can de called repeatedly
    string_len = len(test_string)
    if string_len%2==0: #if the length of the string / 2 has no remainder
        print(f"The length of the string {test_string} is {string_len} and it is even")
    else: #any other situation
        print(f"The length of the string {test_string} is {string_len} and it is odd")

odd_even_checker("Hello")
odd_even_checker("Hellos")
odd_even_checker("Hellosss")
odd_even_checker("Hey")
#calling the function multiple times with different arguements so we can prove our code works


# a list with the alphabet
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

# a for loop - the loop will run for every item in the list - and every time it runs, the variable i represents the current item. The loop will start at the start, end at the end, and move up by one item each time
for i in alpha:
    print(i)

#we need to convert the data type to an integer because input is always a string
answer=int(input("Type a number to see the corresponding letter"))
answer -=1 #so we can take one away from it - if our user wants to see the letter "c" that's the third letter in the alphabet, but it's index position 2 in our list
print(alpha[answer])

