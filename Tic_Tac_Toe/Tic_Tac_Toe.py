import random


class User:
    def __init__(self):
        nam = input("Enter User name : ")
        self.name = nam

    def __str__(self):
        return self.name


def check():
    if lst[0][0] == lst[0][1] and lst[0][0] == lst[0][2] and lst[0][1] == lst[0][2] and lst[0][0] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[1][0] == lst[1][1] and lst[1][0] == lst[1][2] and lst[1][1] == lst[1][2] and lst[1][0] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[2][0] == lst[2][1] and lst[2][0] == lst[2][2] and lst[2][1] == lst[2][2] and lst[2][0] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[0][0] == lst[1][0] and lst[0][0] == lst[2][0] and lst[1][0] == lst[2][0] and lst[0][0] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[0][1] == lst[1][1] and lst[0][1] == lst[2][1] and lst[1][1] == lst[2][1] and lst[0][1] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[0][2] == lst[1][2] and lst[0][2] == lst[2][2] and lst[1][2] == lst[2][2] and lst[0][2] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[0][0] == lst[1][1] and lst[0][0] == lst[2][2] and lst[1][1] == lst[2][2] and lst[1][1] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    if lst[0][2] == lst[1][1] and lst[0][2] == lst[2][0] and lst[1][1] == lst[2][0] and lst[0][2] != '_':
        print("Game has been ended...")
        print("Congratulations!!!")
        for row in lst:
            for col in row:
                print("{}\t".format(col), end="")
            print('')
        quit()
    tot = count(lst)
    if tot == int(0):
        print("No result")
        print("Great! You both done well game is tied..")
        print("Please restart the game..")
        quit()


def position1(data, inp, X):
    inp = int(inp)
    if inp == 1:
        data[0][0] = X
    elif inp == 2:
        data[0][1] = X
    elif inp == 3:
        data[0][2] = X
    elif inp == 4:
        data[1][0] = X
    elif inp == 5:
        data[1][1] = X
    elif inp == 6:
        data[1][2] = X
    elif inp == 7:
        data[2][0] = X
    elif inp == 8:
        data[2][1] = X
    elif inp == 9:
        data[2][2] = X
    else:
        print("Invalid Input!, You lost this chance. Please try in next turn")
    return


def print_lst(data):
    for row in data:
        for col in row:
            print("{}\t".format(col), end="")
        print('')
    return


def count(data):
    co = 0
    for i in range(3):
        for j in range(3):
            if data[i][j] == '_':
                co += 1
    return co


def two_players():
    while True:
        inp1 = int(input("{} Please Enter Position : ".format(player1)))
        position1(lst, inp1, 'X')
        print_lst(lst)
        check()
        inp2 = int(input("{} Please Enter Position : ".format(player2)))
        position1(lst, inp2, 'O')
        print_lst(lst)
        check()


def one_player(data):
    pos = 0
    while True:
        inp1 = int(input("{} Please Enter Position : ".format(player1)))
        position1(data, inp1, 'X')
        print_lst(data)
        check()
        print("Computer turn..")
        _lst = []
        if data[0][0] == 'O' and data[0][1] == 'O' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'O' and data[0][2] == 'O' and data[0][1] == '_':
            position1(data, 2, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'O' and data[0][2] == 'O' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'O' and data[1][1] == 'O' and data[1][2] == '_':
            position1(data, 6, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'O' and data[1][2] == 'O' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'O' and data[1][2] == 'O' and data[1][0] == '_':
            position1(data, 4, 'O')
            print_lst(data)
            check()
        elif data[2][0] == 'O' and data[2][1] == 'O' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[2][0] == 'O' and data[2][2] == 'O' and data[2][1] == '_':
            position1(data, 8, 'O')
            print_lst(data)
            check()
        elif data[2][1] == 'O' and data[2][2] == 'O' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'O' and data[1][0] == 'O' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'O' and data[2][0] == 'O' and data[1][0] == '_':
            position1(data, 4, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'O' and data[2][0] == 'O' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'O' and data[1][1] == 'O' and data[2][1] == '_':
            position1(data, 8, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'O' and data[2][1] == 'O' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'O' and data[2][1] == 'O' and data[0][1] == '_':
            position1(data, 2, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'O' and data[1][2] == 'O' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'O' and data[2][2] == 'O' and data[1][2] == '_':
            position1(data, 6, 'O')
            print_lst(data)
            check()
        elif data[1][2] == 'O' and data[2][2] == 'O' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'O' and data[1][1] == 'O' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'O' and data[2][2] == 'O' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'O' and data[2][2] == 'O' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'O' and data[1][1] == 'O' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'O' and data[2][0] == 'O' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'O' and data[2][0] == 'O' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[0][1] == 'X' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[0][2] == 'X' and data[0][1] == '_':
            position1(data, 2, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'X' and data[0][2] == 'X' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'X' and data[1][1] == 'X' and data[1][2] == '_':
            position1(data, 6, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'X' and data[1][2] == 'X' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'X' and data[1][2] == 'X' and data[1][0] == '_':
            position1(data, 4, 'O')
            print_lst(data)
            check()
        elif data[2][0] == 'X' and data[2][1] == 'X' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[2][0] == 'X' and data[2][2] == 'X' and data[2][1] == '_':
            position1(data, 8, 'O')
            print_lst(data)
            check()
        elif data[2][1] == 'X' and data[2][2] == 'X' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[1][0] == 'X' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[2][0] == 'X' and data[1][0] == '_':
            position1(data, 4, 'O')
            print_lst(data)
            check()
        elif data[1][0] == 'X' and data[2][0] == 'X' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'X' and data[1][1] == 'X' and data[2][1] == '_':
            position1(data, 8, 'O')
            print_lst(data)
            check()
        elif data[0][1] == 'X' and data[2][1] == 'X' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'X' and data[2][1] == 'X' and data[0][1] == '_':
            position1(data, 2, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'X' and data[1][2] == 'X' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'X' and data[2][2] == 'X' and data[1][2] == '_':
            position1(data, 6, 'O')
            print_lst(data)
            check()
        elif data[1][2] == 'X' and data[2][2] == 'X' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[1][1] == 'X' and data[2][2] == '_':
            position1(data, 9, 'O')
            print_lst(data)
            check()
        elif data[0][0] == 'X' and data[2][2] == 'X' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'X' and data[2][2] == 'X' and data[0][0] == '_':
            position1(data, 1, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'X' and data[1][1] == 'X' and data[2][0] == '_':
            position1(data, 7, 'O')
            print_lst(data)
            check()
        elif data[0][2] == 'X' and data[2][0] == 'X' and data[1][1] == '_':
            position1(data, 5, 'O')
            print_lst(data)
            check()
        elif data[1][1] == 'X' and data[2][0] == 'X' and data[0][2] == '_':
            position1(data, 3, 'O')
            print_lst(data)
            check()
        else:
            for i in range(3):
                for j in range(3):
                    if data[i][j] == '_':
                        if i == 0 and j == 0:
                            pos = 1
                        elif i == 0 and j == 1:
                            pos = 2
                        elif i == 0 and j == 2:
                            pos = 3
                        elif i == 1 and j == 0:
                            pos = 4
                        elif i == 1 and j == 1:
                            pos = 5
                        elif i == 1 and j == 2:
                            pos = 6
                        elif i == 2 and j == 0:
                            pos = 7
                        elif i == 2 and j == 1:
                            pos = 8
                        elif i == 2 and j == 2:
                            pos = 9
                        _lst.append(pos)
            comp = random.choice(_lst)
            position1(data, comp, 'O')
            print_lst(data)
            check()


lst = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
players = int(input("Enter no of players : "))
if players == 2:
    player1 = User()
    player2 = User()
    print("The position value and its respective positions")
    print('''1\t2\t3\n4\t5\t6\n7\t8\t9\t''')
    print("Let the fun Begin..")
    print("Welcome {}, Your Symbol is 'X'..".format(player1))
    print("Welcome {}, Your Symbol is 'O'..".format(player2))
    two_players()
elif players == 1:
    player1 = User()
    print("The position value and its respective positions")
    print('''1\t2\t3\n4\t5\t6\n7\t8\t9\t''')
    print("Let the fun Begin..")
    print("Welcome {}, Your Symbol is 'X'..".format(player1))
    one_player(lst)
else:
    print("Please chose at least 1 player and at most 2 players.")
    print("Please try again with valid input..")
