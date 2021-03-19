BOOKED = 1
FREE = 0

NO_SEAT = "NO_SEAT"

seats = {
    "a1": FREE,
    "b1": FREE,
    "c1": FREE,
    "d1": FREE,
    "e1": FREE,
    "f1": FREE,
    "g1": FREE,
    "h1": FREE,
    "i1": FREE,
    "j1": FREE
}


def runTheProgram():
    goToLoop()


def createBooking():
    seatNumber = NO_SEAT
    for key, value in seats.items():
        if value == FREE:
            seats[key] = BOOKED
            seatNumber = key
            break

    if seatNumber == NO_SEAT:
        print("\n\nSorry. No seats are available")
    else:
        print(f"\n\nCongratulations! Your seat is booked and the seat "
              f"number is {seatNumber}")


def viewBookedSeat(userSeatNumber):
    try:
        seatStatus = seats[userSeatNumber]
        if seatStatus == FREE:
            print(f'\n\n{userSeatNumber} is available')
        else:
            print(f'\n\n{userSeatNumber} is booked')
    except KeyError:
        print("\n\nInvalid seat number")


def deleteBooking(seatNumber):
    try:
        seats[seatNumber] = FREE
        print(f'\n\nSuccess. Seat {seatNumber} is now released')
    except ValueError:
        print("\n\nInvalid seat number")


def goToLoop():
    while True:
        print("\n\nWelcome to the Airline Reservation System.")
        print("Type 1 for Create a Booking, \nType 2 to View "
                             "Booking \nType 3 to Delete a Booking \nType 4 "
                             "to Exit")
        option = askAndPrint("Please choose")
        if not validChoice(option):
            print("Not a valid choice.")
            continue

        if option == '1':
            createBooking()

        elif option == '2':
            userSeatNumber = askAndPrint("Please type your seat number")
            viewBookedSeat(userSeatNumber)

        elif option == '3':
            userSeatNumber = askAndPrint("Please type your seat number")
            deleteBooking(userSeatNumber)

        else:
            break

    print("Goodbye! Have a good one")

def validChoice(option):
    try:
        intOption = int(option)
    except ValueError:
        return False

    if intOption == 1:
        return True
    elif intOption == 2:
        return True
    elif intOption == 3:
        return True
    elif intOption == 4:
        return True
    else:
        return False


def askAndPrint(message):
    userInput = input(message + " : ")
    return userInput.lower()


runTheProgram()
