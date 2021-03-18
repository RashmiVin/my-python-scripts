# 
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x))

#display the data type of number:
number = 1 + 2 * 3 / 4.0
print(type(number))

#display the data type
remainder = 11 % 3
print(type(remainder))

#display the data type
squared = 7 ** 2
cubed = 2 ** 3
print(type(squared))
print(type(cubed))

#display the data type
helloworld = "hello" + " " + "world"
print(type(helloworld))

#display the data type
lotsofhellos = "hello" * 10
print(type(lotsofhellos))

#display the data type
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(type(all_numbers))

x= [1,2,3] * 3
print(type(x))

#get the length of the string
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

#get the count of 'l' in the string
astring = "Hello world!"
print(astring.count("l"))

#get the index of 'o' in the string
astring = "Hello world!"
print(astring.index("o"))

#reverse a given string
astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1]) #start:stop:step

#to get true or false
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#to convert into upper case and lower case
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
afewwords = astring.split("Hel")

#Boolean logic
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)