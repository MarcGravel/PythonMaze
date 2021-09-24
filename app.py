import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

board = gameboard.GameBoard()
played = player.Player(3, 2)

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")

    if selection == "w":
        if board.checkMove(played.rowPosition - 1, played.columnPosition):
            played.moveUp()
            print(played.rowPosition, played.columnPosition)
    elif selection == "s":
        if board.checkMove(played.rowPosition + 1, played.columnPosition):
            played.moveDown()
            print(played.rowPosition, played.columnPosition)
    elif selection == "a":
        if board.checkMove(played.rowPosition, played.columnPosition - 1):
            played.moveLeft()
            print(played.rowPosition, played.columnPosition)
    elif selection == "d":
        if board.checkMove(played.rowPosition, played.columnPosition + 1):
            played.moveRight()
            print(played.rowPosition, played.columnPosition)
    else:
        print("Invalid key")

    if board.checkWin(played.rowPosition, played.columnPosition):
        print("You Win!")
        break;

    
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
