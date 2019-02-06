import os
import random


class Ship:

    CBLUE = '\033[34m'
    CWHITE = '\033[37m'
    CEND = '\033[0m'
    board = []
    for i in range(10):
        innerBoard = []
        for j in range(10):
            innerBoard.append(CBLUE + " ~ " + CEND)
        board.append(innerBoard)

    def __init__(self, row, column, orient, holes):
        self.row = row
        self.column = column
        self.orient = orient
        self.holes = holes

    def place_ship(self, num, r, c, o, phH, phV):
        if o.lower() == "h":
            for i in range(num):
                self.board[r][c + i] = phH
        else:
            for i in range(num):
                self.board[r + i][c] = phV

    def display_setup(self):

        self.place_ship(self.holes, self.row, self.column, self.orient, "===", "|||")

        print(self.CWHITE + "     1  2  3  4  5  6  7  8  9  10" + self.CEND)
        lets = "a b c d e f g h i j"
        lets = lets.split()
        for i in range(len(self.board)):
            tem = "".join(self.board[i])
            print self.CWHITE, lets[i], self.CEND, tem


class Board:

    CBLUE = '\033[34m'
    CWHITE = '\033[37m'
    CEND = '\033[0m'

    def __init__(self, carrier, battleship, cruiser, submarine, destroyer):
        # making grid
        board = []
        for i in range(10):
            innerBoard = []
            for j in range(10):
                innerBoard.append(self.CBLUE + " ~ " + self.CEND)
            board.append(innerBoard)

        self.board = board
        self.carrier = carrier
        self.battleship = battleship
        self.cruiser = cruiser
        self.submarine = submarine
        self.destroyer = destroyer

    def place_ship(self, num, r, c, o, frontH, middleH, backH, frontV, middleV, backV):
        if o.lower() == "h":
            self.board[r][c] = frontH
            for i in range(1, num):
                self.board[r][c + i] = middleH
            self.board[r][c + num] = backH
        else:
            self.board[r][c] = frontV
            for i in range(1, num):
                self.board[r + i][c] = middleV
            self.board[r + num][c] = backV

    def display_board(self):

        self.place_ship(4, self.carrier.row, self.carrier.column, self.carrier.orient, "[--", "===", "-P]", "[ ]", "|||", "[_]")
        self.place_ship(3, self.battleship.row, self.battleship.column, self.battleship.orient, "<{]", "={]", "[]>", "|^|", "|*|", "[=]")
        self.place_ship(2, self.cruiser.row, self.cruiser.column, self.cruiser.orient, "<=[", "]==", "[]>", "|^|", "| |", "[+]")
        self.place_ship(2, self.submarine.row, self.submarine.column, self.submarine.orient, "(==", "==o", "==)", "( )", "|o|", "( )")
        self.place_ship(1, self.destroyer.row, self.destroyer.column, self.destroyer.orient, "<={", "={]", "[]>", "(^)", "|^|", "[=]")

        print(self.CWHITE + "     1  2  3  4  5  6  7  8  9  10" + self.CEND)
        lets = "a b c d e f g h i j"
        lets = lets.split()
        for i in range(len(self.board)):
            tem = "".join(self.board[i])
            print self.CWHITE, lets[i], self.CEND, tem


def check(num, holes, rORc):
    if rORc == "row":
        while num > 10 - holes:
            print "Your row is invalid"
            num = raw_input("please try again: ")
            while num not in lets:
                print("Your row is invalid")
                num = raw_input("try again: ")
            num = lets.index(num)+1
    else:
        while not num.isdigit():
            num = raw_input("please enter a number: ")
        num = int(num)
        while num > 11 - holes:
            print "Your column number is invalid"
            num = raw_input("please try again: ")
            while not num.isdigit():
                num = raw_input("please enter a number: ")
            num = int(num)

    return num-1


def check_overlap(orientation, row, column, holes):
    lap = False
    points = []
    if orientation == "h":
        for i in range(holes):
            points.append([row, column+i])
    else:
        for i in range(holes):
            points.append([row+i, column])

    for i in points:
        if i in taken:
            lap = True
    if lap:
        print "your ships overlap, try different points."
    return lap


def build_ship(ship, holes):
    # row, column, orientation
    o_q = ship + " orientation H/V: "
    r_q = ship + " row: "
    c_q = ship + " column: "
    valid = True
    while valid:
        orientation = raw_input(o_q)
        if orientation.lower() == "h":
            lap = True
            while lap:
                row = raw_input(r_q)
                while row not in lets:
                    print("Your row is invalid")
                    row = raw_input("try again: ")
                row = lets.index(row)

                column = raw_input(c_q)
                column = check(column, holes, "column")
                lap = check_overlap("h", row, column, holes)

            for i in range(holes):
                taken.append([row, column+i])
            valid = False

        elif orientation.lower() == "v":
            lap = True
            while lap:
                row = raw_input(r_q)
                while row not in lets:
                    print("Your row is invalid")
                    row = raw_input("try again: ")
                row = lets.index(row)+1
                row = check(row, holes-1, "row")

                column = raw_input(c_q)
                while not column.isdigit():
                    print("Your column number is invalid")
                    column = raw_input("please enter a number 1-10: ")
                column = int(column)-1
                lap = check_overlap("v", row, column, holes)

            for i in range(holes):
                taken.append([row+i, column])
            valid = False

        else:
            print("please enter a valid orientation")

    return Ship(row, column, orientation, holes)


def make_player_board():

    carrier = build_ship("carrier", 5)
    os.system("clear")
    Ship.display_setup(carrier)
    battleship = build_ship("battleship", 4)
    os.system("clear")
    Ship.display_setup(battleship)
    cruiser = build_ship("cruiser", 3)
    os.system("clear")
    Ship.display_setup(cruiser)
    submarine = build_ship("submarine", 3)
    os.system("clear")
    Ship.display_setup(submarine)
    destroyer = build_ship("destroyer", 2)
    os.system("clear")

    return Board(carrier, battleship, cruiser, submarine, destroyer)


def generate_ship(holes):
    orientation = random.randint(1, 2)
    if orientation == 1:
        orientation = "h"
        lap = True
        while lap:
            row = random.randint(1, 9)
            column = random.randint(1, 9 - holes)
            points = []
            for i in range(holes):
                points.append([row, column+i])

            x = 0
            for i in points:
                if i in cpuTaken:
                    x += 1
            if x < 1:
                lap = False

        for i in range(holes):
            cpuTaken.append([row, column+i])

    else:
        orientation = "v"
        lap = True
        while lap:
            row = random.randint(1, 9 - holes)
            column = random.randint(1, 9)
            points = []
            for i in range(holes):
                points.append([row+i, column])

            x = 0
            for i in points:
                if i in cpuTaken:
                    x += 1
            if x < 1:
                lap = False

        for i in range(holes):
            cpuTaken.append([row+i, column])
    return Ship(row, column, orientation, holes)


def make_cpu_board():
    carrier = generate_ship(5)
    battleship = generate_ship(4)
    cruiser = generate_ship(3)
    submarine = generate_ship(3)
    destroyer = generate_ship(2)

    return Board(carrier, battleship, cruiser, submarine, destroyer)


def main():
    global taken
    taken = []
    global cpuTaken
    cpuTaken = []
    CBLUE = '\033[34m'
    CWHITE = '\033[37m'
    CEND = '\033[0m'

    os.system("clear")
    board = []
    for i in range(10):
        innerBoard = []
        for j in range(10):
            innerBoard.append(CBLUE + " ~ " + CEND)
        board.append(innerBoard)

    print(CWHITE + "     1  2  3  4  5  6  7  8  9  10" + CEND)
    global lets
    lets = "a b c d e f g h i j"
    lets = lets.split()
    for i in range(len(board)):
        tem = "".join(board[i])
        print CWHITE, lets[i], CEND, tem

    board1 = make_player_board()
    board1.display_board()
    x = raw_input("HIT ENTER TO CONTINUE")

    cpuBoard = make_cpu_board()
    cpuBoard.display_board()


main()
