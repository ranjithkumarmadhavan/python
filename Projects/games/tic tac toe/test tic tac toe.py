board = [' ' for i in range(10)]

def displayBoard():
    print("   |   |")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-'*11)
    print("   |   |")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-'*11)
    print("   |   |")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def makeMove(position, char):
    board[position] = char

def isBoardEmpty():
    return board.count(' ') > 1

def isWinner(bo,le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[7] == le and bo[8] == le and bo[9] == le)) 

def main():
    print("Welcome to tic tac toe")
    displayBoard()
    while not isBoardEmpty():
        select = input("Your Move ('X'). Select any number from [1-9]")
        makeMove(select,'X')
        if isWinner(board,'X'):
            print("'X' is the winner")
            break
        
        # makeMove(1,'X')
        # displayBoard()
        # break

main()