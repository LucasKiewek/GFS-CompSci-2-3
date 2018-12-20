import os


class Ship:

    # ship class
    def __init__(self, row, column, orient, holes):
        self.row = row
        self.column = column
        self.orient = orient
        self.holes = holes




class Board:

    # making grid
    board = []
    for i in range(10):
        innerBoard = []
        for j in range(10):
            innerBoard.append(" ~ ")
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
        self.place_ship(3, self.battleship.row, self.battleship.column, self.battleship.orient, "<{]", "={]", "[]>", " ^ ", "|*|", "[=]")
        self.place_ship(2, self.cruiser.row, self.cruiser.column, self.cruiser.orient, "<=[", "]==", "[]>", " ^ ", "| |", "[+]")
        self.place_ship(2, self.submarine.row, self.submarine.column, self.submarine.orient, "(==", "==o", "==)", "( )", "|o|", "( )")
        self.place_ship(1, self.destroyer.row, self.destroyer.column, self.destroyer.orient, "<={", "={]", "[]>", " ^ ", "|^|", "[=]")

        print("\t 1  2  3  4  5  6  7  8  9  10")
        for i in range(len(self.board)):
            tem = "".join(self.board[i])
            print i+1, "\t", tem


def check(num, holes):
    while (num < 10 - holes) or (not num.isdigit()):
        print("Your number is invalid")
        num = raw_input("please try again: ")

    return int(num)-1


def build_ship(ship, holes):
    # row, column, orientation
    o_q = ship + " orientation H/V: "
    r_q = ship + " row: "
    c_q = ship + " column: "
    valid = True
    while valid:
        orientation = raw_input(o_q)
        if orientation.lower() == "h":
            row = raw_input(r_q)
            while not row.isdigit():
                print("Your row number is invalid")
                row = raw_input("please enter a number 1-10: ")
            row = int(row)-1

            column = raw_input(c_q)
            column = check(column, holes)
            os.system("clear")
            for i in range(holes):
                taken.append([row, column+i])
            valid = False

        elif orientation.lower() == "v":
            column = raw_input(c_q)
            while not column.isdigit():
                print("Your column number is invalid")
                column = raw_input("please enter a number 1-10: ")
            column = int(column)-1

            row = raw_input(r_q)
            row = check(row, holes)
            os.system("clear")
            for i in range(holes):
                taken.append([row+i, column])
            valid = False

        else:
            os.system("clear")
            print("please enter a valid orientation")

    return Ship(row, column, orientation, holes)


def main():
    global taken
    taken = []

    carrier = build_ship("carrier", 5)
    battleship = build_ship("battleship", 4)
    cruiser = build_ship("cruiser", 3)
    submarine = build_ship("submarine", 3)
    destroyer = build_ship("destroyer", 2)

    board = Board(carrier, battleship, cruiser, submarine, destroyer)
    board.display_board()


main()
