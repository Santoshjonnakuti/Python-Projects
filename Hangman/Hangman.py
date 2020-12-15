# importing everything from tkinter
from tkinter import *
# importing ImageTk, Image from PIL to set the background of the window
from PIL import ImageTk, Image
# importing random to select random image for background and a random word from the wordList
import random
global length
global word, score
global hideString, index, duplicate

# Predefined list of words
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


# Function to create a dictionary with key=letter in word and value=count of a particular letter
def makeDiction(Word):
    dictionary = {}
    for letter in Word:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary


def letterButtonSubmitFunc():
    global word, score
    score = int(labelScoreValue['text'])
    # Assigning the color of labelScoreValue as per the score
    if score == 75:
        labelScoreValue['fg'] = "yellow"
    elif score == 50:
        labelScoreValue['fg'] = "orange"
    elif score == 35:
        labelScoreValue['fg'] = "red"
    global hideString, index
    Dictionary = makeDiction(word)
    Word = word
    letterString = hideString
    letter = letterInput.get()
    messageLabel.place_forget()
    letterSubmitButton.place(relx=0.5, rely=0.6, anchor="center")
    # Checking whether the user entered a character or not
    try:
        len(letter)
        if letter.lower() in Word:
            if Dictionary[letter.lower()] != 0:
                Dictionary[letter.lower()] = Dictionary[letter.lower()] - 1
                index = word.find(letter.lower(), 0, len(Word))
                if index == 0:
                    Word = '*' + Word[1:]
                elif index == (len(Word)-1):
                    Word = Word[0:len(Word)-1] + '*'
                else:
                    Word = Word[0:index] + '*' + Word[index+1:]
            letterString = letterString[0:index] + letter.lower() + letterString[index+1:]
            wordLabel['text'] = letterString
        elif letter.lower() not in Word and letter.lower() in Dictionary:
            messageLabel['text'] = "You guessed all {}'s in the word...".format(letter.lower())
            messageLabel.place(relx=0.5, rely=0.6, anchor="center")
            letterSubmitButton.place(relx=0.5, rely=0.7, anchor="center")
        # if guessed letter not in word
        else:
            messageLabel['text'] = "You guessed it wrong...\nTry again..."
            labelScoreValue['text'] = str(int(labelScoreValue['text']) - 5)
            messageLabel.place(relx=0.5, rely=0.6, anchor="center")
            letterSubmitButton.place(relx=0.5, rely=0.7, anchor="center")
            if score == 5:
                labelScore.place_forget()
                labelScoreValue.place_forget()
                wordLabel.place_forget()
                letterInput.place_forget()
                letterSubmitButton.place_forget()
                guessLabel.place_forget()
                messageLabel['fg'] = "red"
                messageLabel['text'] = "You lost\n Word is {}".format(duplicate)
                messageLabel.place(relx=0.5, rely=0.5, anchor="center")
        # if all letters are guessed
        if letterString.count('*') == 0:
            messageLabel['text'] = "Hurray! You guessed the word right!!\nCongratulations!!!\nYour Score is {}".format(score)
            guessLabel.place_forget()
            letterInput.place_forget()
            messageLabel.place(relx=0.5, rely=0.4, anchor="center")
            letterSubmitButton.place(relx=0.5, rely=0.5, anchor="center")
            letterSubmitButton['state'] = DISABLED
    # If user entered nothing then displaying a message
    except KeyError:
        messageLabel['text'] = "Enter a letter"
        messageLabel.place(relx=0.5, rely=0.6, anchor="center")
        letterSubmitButton.place(relx=0.5, rely=0.7, anchor="center")
    letterInput.delete(0, END)
    hideString = letterString
    word = Word


def submitButtonFunc():
    # Checking whether the length is a integer or not
    try:
        int(wordlength.get())
        global length, hideString

        length = wordlength.get()
        if 3 <= int(wordlength.get()) <= 8:
            # Deleting some of the widgets from the screen
            labellength.place_forget()
            submitButton.place_forget()
            wordlength.place_forget()
            labelError.place_forget()
            wordLabel.place(relx=0.5, rely=0.3, anchor="center")
            global word
            # Choosing a random word from the wordList
            word = random.choice(wordList[int(length)])
            global duplicate
            duplicate = word
            # Creating a string with '*'
            hideString = ''
            for _ in word:
                hideString = hideString + '*'
            # Changing the text value of word label to hideString
            wordLabel['text'] = hideString
            guessLabel.place(relx=0.5, rely=0.4, anchor="center")
            letterInput.place(relx=0.5, rely=0.5, anchor="center")
            letterSubmitButton.place(relx=0.5, rely=0.6, anchor="center")
        # Displaying a message if the length is not in between 3 and 8
        else:
            labelError['text'] = "Length of the word should be in between 3 and 8"
            labelError['fg'] = "red"
            labelError.place(relx=0.5, rely=0.6, anchor="center")
            submitButton.place(relx=0.5, rely=0.7, anchor="center")
    # Displaying a message if the user entered a character
    except ValueError:
        labelError['text'] = "Length of the word should be a integer"
        labelError['fg'] = "red"
        labelError.place(relx=0.5, rely=0.6, anchor="center")
        submitButton.place(relx=0.5, rely=0.7, anchor="center")


def play_button_func():
    # Deleting the label from the tkinter window
    label2.place_forget()
    # Deleting the Play button from the tkinter window after clicking the button
    play_button.place_forget()
    # Adding Score label to the Screen
    labelScore.place(relx=0.005, rely=0.005, anchor="nw")
    # Adding Score value label to the screen
    labelScoreValue.place(relx=0.08, rely=0.005)
    # Adding the Label to the screen
    labellength.place(relx=0.5, rely=0.4, anchor="center")
    # Adding the input box to the screen
    wordlength.place(relx=0.5, rely=0.5, anchor="center")
    submitButton.place(relx=0.5, rely=0.6, anchor="center")
    global length
    # Storing the length of the word in the variable length
    length = wordlength.get()


# Creating a tkinter window
root = Tk()
# Assigning title to the window
root.title("Hangman")
# Fixing the size of the window
root.resizable(0, 0)
# Setting the icon for the window
root.iconbitmap("C:\\Users\\hp\\Documents\\Games\\Hangman\\Hangman-Game-grey.ico")
# Opening the images
bgImage1 = Image.open('C:\\Users\\hp\\Documents\\Games\\Hangman\\HangmanBg.jpg')
bgImage2 = Image.open('C:\\Users\\hp\\Documents\\Games\\Hangman\\HangmanBg1.jpg')
bgImage3 = Image.open('C:\\Users\\hp\\Documents\\Games\\Hangman\\HangmanBg2.jpg')
bgList = [bgImage1, bgImage2, bgImage3]
# Choosing a random image from the bgList to set background
image1 = ImageTk.PhotoImage(random.choice(bgList))
# Creating a label with the random image
label1 = Label(root, image=image1)
# Adding image to the tkinter window
label1.pack()
# Label to display the welcome message
label2 = Label(root, text="Welcome to Hangman", bg="black", fg="white", font=("Helvetica", 30), bd=10, relief=RAISED)
label2.place(relx=0.5, rely=0.005, anchor="n")
# Button to start the game
play_button = Button(root, text="Play", bg="black", fg="white", font=("Helvetica", 15), bd=8, command=play_button_func)
play_button.place(relx=0.5, rely=0.7, anchor=CENTER)
# Label to display the Score
labelScore = Label(root, text="Score", bg="black", fg="white", font=("Helvetica", 15))
# Label to display the Score Value
labelScoreValue = Label(root, text="100", bg="black", fg="green", font=("Helvetica", 15))
# Label to display an instruction to the player
labellength = Label(root, text="Enter the length of the word (3 to 8)", font=("Helvetica", 15))
# Input box to enter the length of the word
wordlength = Entry(root, width=20, font=("Helvetica", 15))
# Label to display the Error message
labelError = Label(root, text="Length of the word should be in between 3 and 8", font=("Helvetica", 15))
# Button to submit the length of the word
submitButton = Button(root, text="Submit", command=submitButtonFunc)
# Button to Quit from the game
quitButton = Button(root, text="Quit", bg="black", fg="white", font=("Helvetica", 15), command=root.quit)
quitButton.place(relx=0.5, rely=0.9, anchor="center")
# Word label to display the selected word with '*'
wordLabel = Label(root, text="Searching Word...", bg="white", fg="black", font=("Helvetica", 15))
# Input box to enter letter by the player
letterInput = Entry(root, width=20, font=("Helvetica", 15), fg="black", bg="white")
# Label to display the message
guessLabel = Label(root, text="Guess a letter in the word...", fg="black", bg="white", font=("Helvetica", 15))
# Label to display the feedback of the letter entered
messageLabel = Label(root, text="", bg="white", fg="green", font=("Helvetica", 15))
# Button to submit the entered letter
letterSubmitButton = Button(root, text="Submit", command=letterButtonSubmitFunc)
# Running a loop for the tkinter window
root.mainloop()
