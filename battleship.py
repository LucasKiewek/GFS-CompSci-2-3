import os


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

        print(self.CWHITE + "\t 1  2  3  4  5  6  7  8  9  10" + self.CEND)
        for i in range(len(self.board)):
            tem = "".join(self.board[i])
            print self.CWHITE, i+1, self.CEND, "\t", tem




class Board:

    # making grid
    CBLUE = '\033[34m'
    CWHITE = '\033[37m'
    CEND = '\033[0m'
    board = []
    for i in range(10):
        innerBoard = []
        for j in range(10):
            innerBoard.append(CBLUE + " ~ " + CEND)
        board.append(innerBoard)

    def __init__(self, carrier, battleship, cruiser, submarine, destroyer):
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

        print(self.CWHITE + "\t 1  2  3  4  5  6  7  8  9  10" + self.CEND)
        for i in range(len(self.board)):
            tem = "".join(self.board[i])
            print self.CWHITE, i+1, self.CEND, "\t", tem


def check(num, holes, rORc):
    while not num.isdigit():
        num = raw_input("please enter a number: ")
    num = int(num)
    while num > 10 - holes:
        print "Your", rORc, "number is invalid"
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
                while not row.isdigit():
                    print("Your row number is invalid")
                    row = raw_input("please enter a number 1-10: ")
                row = int(row)-1

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


def main():
    global taken
    CBLUE = '\033[34m'
    CWHITE = '\033[37m'
    CEND = '\033[0m'
    taken = []

    os.system("clear")
    board = []
    for i in range(10):
        innerBoard = []
        for j in range(10):
            innerBoard.append(CBLUE + " ~ " + CEND)
        board.append(innerBoard)

    print(CWHITE + "\t 1  2  3  4  5  6  7  8  9  10" + CEND)
    for i in range(len(board)):
        tem = "".join(board[i])
        print CWHITE, i+1, CEND, "\t", tem

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

    board1 = Board(carrier, battleship, cruiser, submarine, destroyer)
    board1.display_board()


main()
