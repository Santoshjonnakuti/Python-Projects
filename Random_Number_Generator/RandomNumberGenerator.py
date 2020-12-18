import random
global tup


def generateTuple(n):
    lst = [(0, 30), (10, 40), (20, 50), (30, 60), (40, 70), (50, 80), (60, 90), (70, 100)]
    rlist = []
    for item in lst:
        if item[0] <= n <= item[1]:
            rlist.append(item)
    return rlist


def Hint(choice, num):
    if choice == 2:
        if num % 2 == 0:
            print("Hint 2 : Number is Even")
        else:
            print("Hint 2 : Number is Odd")
    elif choice == 3:
        lst = generateTuple(num)
        global tup
        tup = random.choice(lst)
        print("Hint 3 : Number is greater than or equal to {}".format(tup[0]))
    elif choice == 4:
        print("Hint 4 : Number is less than or equal to {}".format(tup[1]))
    elif choice == 5:
        remainder = num % 4
        print("Hint 5 : Remainder is {} when divided by 4".format(remainder))
    elif choice == 6:
        remainder = num % 6
        print("Hint 7 : Remainder is {} when divided by 6".format(remainder))
    elif choice == 7:
        remainder = num % 7
        print("Hint 8 : Remainder is {} when divided by 7".format(remainder))
    elif choice == 8:
        remainder = num % 5
        print("Hint 9 : Remainder is {} when divided by 5".format(remainder))
    elif choice == 9:
        remainder = num % 3
        print("Hint 10 : Remainder is {} when divided by 3".format(remainder))
    else:
        print("Refer to the Hints above...")


number = random.randint(1, 100)
print('''Instructions :
Your score is 100 at the start of the game...
Your score will get reduced by 1 if you guess the number wrong...
Your will get a hint after each guess and first guess...
Lets get Started...''')

score = 100
chance = 0
print("Hint 1 : Number is in between 0 and 100(including both 0 and 100)")

while True:
    userInput = int(input("Guess the Number : "))
    chance += 1
    if userInput == number:
        print("You guessed it right...\nYour score is {}".format(score))
        quit()
    elif score == 0 or chance == 10:
        print("Your Guesses are wrong \nYou lost...\nPlease try again...")
        print("The number is " + str(number))
        quit()
    else:
        score -= 10
        Hint(chance, number)
