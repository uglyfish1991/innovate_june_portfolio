print("this is dictionaries")

#dictionaries let us store key:value pairs
#we use {} around dictionaries
# a dictionary saved to the variable "my_cat"
my_cat = {
    "name":"Salem",
    "colour":"Black",
    "mood": "Sassy"
}

# a dictionary saved to the variable "my_dog"
my_dog = {
    "name":"Toby",
    "breed":"Keeshond",
    "mood":"Barky"
}
#the keys are the first things - in this case name, breed, mood - the values are the second.

print(my_dog["mood"]) #selecting a value using a key instead of index

my_dog["mood"] = "hungry" # using that method to update a value
my_dog["age"]=2 #or creating the key if it doesn't exist yet
print(f'My dog \"{my_dog["name"]}\" is a bit {my_dog["mood"]} today')

#dictionaries have methods just like lists. Dictionaries are muteable - they can change, so we can use methods to do that

print(my_dog.keys())
#returns us a view object with all the keys in our list!

print(my_dog.values())
#returns us a view object with all the values in our list!

print(my_dog.items())
#returns us a view object with all the items in our list!

# the get meothd allows us to get the value of a key:
# print(my_dog.get("keygoeshere"))
# print(my_dog.get("mood"))
#we did this earlier with print(my_dog["mood"]) - so why is .get() different?

# if we start searching for a key that doesn't exist - the square brackets will give us an error and stop our code!
# the .get() method will return us the blank data type "None"

print(my_dog.get("legs")) #<- this will work!
# print(my_dog["legs"]) <- this will not!

#we can also give a second arguement to get - a customer error message / bit of data rather than "none"
print(my_dog.get("legs","This key does not exist")) #<- this will work!

#we can use the .update() method to add or update keys and values in our list!
my_dog.update({"legs":"4"})
my_dog.update({"name":"Professor Tobias"})
print(my_dog)

#and .pop() to remove keys - and their values will go too
my_dog.pop("mood")
print(my_dog)

#viewing a dictionary isn't the nicest in a terminal!

print(my_dog.keys()) #prints it normally - as a "view object"
print(list(my_dog.keys())) #converts the view object to a list!

# or we could use a handy for loop - because this is iterable!
for every_key in my_dog.keys():
    print(every_key)