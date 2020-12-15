import random
from time import sleep

global length


def _input():
    global length

    length = input("Enter the length of the word you wanna find : ")
    try:
        length = int(length)
    except ValueError:
        print("Invalid input length must be a integer...")
        _input()
    if 3 <= length <= 8:
        pass
    else:
        print("Enter a valid input as per the instructions..")
        _input()


def makeDiction():
    dictionary = {}
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary


def play(Word, dictionar):
    string = ''
    global length
    length = int(length)
    for j in range(length):
        string = string + '*'
    print(string)
    while string.count('*') != 0:
        letter = input("Guess a letter in the word : ")
        if letter.lower() in Word:
            if dictionar[letter.lower()] != 0:
                dictionar[letter.lower()] = dictionar[letter.lower()] - 1
                index = Word.find(letter.lower(), 0, len(Word))
                if index == 0:
                    Word = '*' + Word[1:]
                elif index == (len(Word)-1):
                    Word = Word[0:len(Word)-1] + '*'
                else:
                    Word = Word[0:index] + '*' + Word[index+1:]
                string = string[0:index] + letter.lower() + string[index+1:]
                print(string)
        elif letter.lower() not in Word and letter.lower() in dictionar:
            print("You guessed all {}'s in the word...".format(letter))
            print(string)
        else:
            print("You guessed it wrong..\nTry again...")
            print(string)
    if string.count('*') == 0:
        print("Hurray! You guessed the word right!!\nCongratulations!!!")
    return


wordList = [[], [], [], ['and', 'are', 'off', 'key', 'why', 'how', 'you', 'fox', 'ate', 'now'],
            ['four', 'five', 'gone', 'huge',
             'good', 'then', 'what', 'when',
             'bear', 'your'],
            ['eight', 'super', 'great', 'fifty', 'tools', 'wrong',
             'right', 'solve', 'codes', 'space'], ['window', 'charge', 'python', 'twelve', 'abroad', 'access', 'active',
                                                   'belief', 'camera', 'decent'],
            ['ability', 'console', 'address', 'classes', 'deposit', 'essence', 'further',
             'license', 'passing', 'mixture'], ['absolute', 'abstract', 'terminal', 'navigate', 'collapse', 'disaster',
                                                'external', 'frequent', 'literary', 'platform']]
print("Welcome to Hangman")
name = input("Enter your name : ")
print("Welcome {}\nInstructions:\n1. The length of the word should be in between 3 and 8".format(name))
_input()
print("Searching word...")
sleep(2)
for i in range(3, 9):
    if i == length:
        word = random.choice(wordList[i])
    else:
        continue
print("Word is selected...")
diction = makeDiction()
sorted(diction)
print(word)
print(diction)
play(word, diction)
