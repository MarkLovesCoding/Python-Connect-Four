import numpy
ROWS = 6
COLUMNS = 7
# Columns,  6 x 7
def create_board():
    board = numpy.zeros((ROWS,COLUMNS))
    return board


board = create_board()
def print_board(board):
    print(numpy.flip(board,0))



game_over = False
player_turn = 1

def check_win(board):
#     # check horizontal for 4 across
    for r in board:
        for c in range(len(r)-3):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] :
                    print("Player ", str(r[c])[0]," wins!")
                    return True
    # vertical check
    for r in range(len(board) - 3):
        for c in range(len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    print("Player ", str(board[r][c])[0]," wins!")
                    return True
    # positive diagonal
    for r in range(len(board) - 3):
        for c in range(len(board[r] - 3)):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    print("Player ", str(board[r][c])[0]," wins!")
                    return True

    # negative diagonal NEEDS FIXING
    for r in range(len(board)-3):
        for c in range(3, len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    print(print("Player ", str(board[r][c])[0]," wins!"))
                    return True
                    
def is_valid_column(board,col):
    if int(board[0][col]) == 0:
        return True
    else:
        return False

# print(is_valid_column(board,2))
def drop_piece(board,col,player):
    if is_valid_column(board,col):
        for r in range(len(board)-1,-1,-1):
            if board[r][col] == 0:
                board[r][col] = player
                return True
    else:
        print("Column full. Please try another column.")
        return False

def input_column(board, player):
    player_input = 0
    while player_input >= 8 or player_input <= 0:
    
            try:    
                player_input = int(input("Player "+str(player)+" Choose a column (1-7):"))
                # print(player_input)
                if player_input > 0 and player_input < 8:
                    # print(player)
                    player_input -= 1
                    if(drop_piece(board,player_input,player)):
                        print(board)
                        return True
                        # break
                    else:
                        return False
                else:
                    print("Please input integer between 1-7")
                
            except:
                print("Please input integer between 1-7, inclusive")

  

def play(game_over,player_turn,board):
    print(board)
    while not game_over:
        # Get input for player 1
       
        if player_turn == 1:
            if input_column(board,1) == True:
                player_turn = 2
                if(check_win(board)):
                    break

            else:
                # input_column(board,1)
                player_turn = 1

        if player_turn == 2:
            if input_column(board,2) == True:
                player_turn = 1
                if(check_win(board)):
                    break
            else:
                player_turn = 2
        

# print(print_board(board))
play(game_over,player_turn,board)
