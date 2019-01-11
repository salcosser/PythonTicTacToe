# Python Tic Tac Toe
# Sam Alcosser


class Game:

    # the function that gets executed when an instace of the class is formed
    def __init__(self, rowA, rowB, rowC, complete):
        self.rowA = rowA
        self.rowB = rowB
        self.rowC = rowC
        self.complete = complete

    def move(self, row, place, team):
        if row[place] == "-":
            row[place] = team
            print(self.rowA)
            print(self.rowB)
            print(self.rowC)
        else:
            print("place previously taken")
            print(self.rowA)
            print(self.rowB)
            print(self.rowC)
        # huuuuge list of conditional statements

        # straight across row 1

        if game1.rowA[0] == game1.rowA[1] == game1.rowA[2] and game1.rowA[0] != "-":
            game1.complete = True
            print(str(game1.rowA[0]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format")
            print("game1.move(game1.row, place, team)")

        # straight across row 2
        elif game1.rowB[0] == game1.rowB[1] == game1.rowB[2] and game1.rowB[0] != "-":
            game1.complete = True
            print(str(game1.rowB[0]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

        # straight across row three
        elif game1.rowC[0] == game1.rowC[1] == game1.rowC[2] and game1.rowC[0] != "-":
            game1.complete = True
            print(str(game1.rowC[0]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

            # straight down column 1
        elif game1.rowA[0] == game1.rowB[0] == game1.rowC[0] and game1.rowA[0] != "-":
            game1.complete = True
            print(str(game1.rowA[0]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

        # straight down column 2
        elif game1.rowA[1] == game1.rowB[1] == game1.rowC[1] and game1.rowA[1] != "-":
            game1.complete = True
            print(str(game1.rowA[1]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

        # straight down column 3
        elif game1.rowA[2] == game1.rowB[2] == game1.rowC[2] and game1.rowA[2] != "-":
            game1.complete = True
            print(str(game1.rowA[2]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

        # diagonal starting top left
        elif game1.rowA[0] == game1.rowB[1] == game1.rowC[2] and game1.rowA[0] != "-":
            game1.complete = True
            print(str(game1.rowA[0]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                  "place, team)")

        # diagonal starting top right
        elif game1.rowA[2] == game1.rowB[1] == game1.rowC[0] and game1.rowA[2] != "-":
            game1.complete = True
            print(str(game1.rowA[2]) + " Wins!!!")
            print("to restart, type game1.restart() ")
            print(game1.rowA)
            print(game1.rowB)
            print(game1.rowC)
            print("    *-----*\n")
            print(
                "to make a move, type your desired row, column, and team with this format; game1.move(game1.row, "
                "place, team)")

    def restart(self):
        self.rowA = ['-', '-', '-']
        self.rowB = ['-', '-', '-']
        self.rowC = ['-', '-', '-']
        print(self.rowA)
        print(self.rowB)
        print(self.rowC)


# game instantiation
game1 = Game(['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], False)

print("tic tac toe through python!!! \n")
print(game1.rowA)
print(game1.rowB)
print(game1.rowC)
print("    *-----*\n")
# this program works if the prompts and conditional statement below are commented out
print("to make a move, type your desired row, column, and team with this format; game1.move(game1.row, place, team)")
# if game1.complete == False and row[place] != "-":
#  row = "game1." + input("which row, rowA, rowB, or rowC?")
# column = int(input("What column, 0, 1, or 2?"))
#  team = input("what team? x or o?")
# game1.move(row, column, team)
# else:
#       print("place previously taken")
#       print(self.rowA)
#       print(self.rowB)
#      print(self.rowC)
