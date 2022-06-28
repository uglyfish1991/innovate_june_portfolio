# # test_string = "Welcome to Code Nations"



# def odd_even_checker(test_string):
#     string_len = len(test_string)
#     if string_len%2==0:
#         print(f"The length of the string {test_string} is {string_len} and it is even")
#     else:
#         print(f"The length of the string {test_string} is {string_len} and it is odd")

# odd_even_checker("Hello")
# odd_even_checker("Hellos")
# odd_even_checker("Hellosss")
# odd_even_checker("Hey")

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

for i in alpha:
    print(i)

answer=int(input("Type a number to see the corresponding letter"))
answer -=1
print(alpha[answer])