import time
import random

print("Hello, welcome to the arcade")
time.sleep(2.4)

count = 0
summ = 0

list1 = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 10
}
while count < 3:
    pick = key, val = random.choice(list(list1.items()))
    print("Your card is picked. You are dealt a ", pick[0], "It's value is ", pick[1])
    input("Hit enter to continue")
    summ = summ + int(pick[1])
    count = count + 1
#print("Total value is ", summ)
if summ==21:
    print("Almost there, try again")
elif summ<21:
    print("Oops, please try again")
else:
    print("Congratulations you are a Millionaire")



