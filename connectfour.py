import numpy
import random

# INITIALIZE ROWS/COLUMNS VARS
ROWS = 6
COLUMNS = 7

def create_board():
    board = numpy.zeros((ROWS,COLUMNS))
    return board

# INITIALIZE OTHER VARS
game_over = False
player_turn = 1
# board = create_board()
intro_banner="""
  #####  ####### #     # #     # #######  #####  #######    ####### ####### #     # ######  
 #     # #     # ##    # ##    # #       #     #    #       #       #     # #     # #     # 
 #       #     # # #   # # #   # #       #          #       #       #     # #     # #     # 
 #       #     # #  #  # #  #  # #####   #          #       #####   #     # #     # ######  
 #       #     # #   # # #   # # #       #          #       #       #     # #     # #   #   
 #     # #     # #    ## #    ## #       #     #    #       #       #     # #     # #    #  
  #####  ####### #     # #     # #######  #####     #       #       #######  #####  #     # 
\n\nHow Many Players (1 or 2)?"""

# print board with columns
def print_board(board):
    print(board)
    print("  1  2  3  4  5  6  7  ")

# random column for computer move (basic easy 1 player game)
def computer_player_move():
    column = random.randint(0,6)
    return column

# standard starting
# how_many = 2
how_many_players = 2
# play game
def intro():
    board = create_board()
    how_many = input(intro_banner)
    # 2 player game
    if how_many == "2" or how_many == 2:
        how_many_players = 2
        play(game_over,player_turn,board,how_many_players)
    # 1 player game
    if how_many == "1" or how_many == 1:
        how_many_players = 1
        play(game_over,player_turn,board,how_many_players)
    # default to 2 player
    if how_many != "2" or how_many != 2 or how_many != "1" or how_many != 1:
        # how_many_players = 2
        print("\n")
        print("You typed:",how_many, ". \nThat's not a 1 or a 2, silly.\n  Let's try that again.")
        intro()
        # board = create_board()
        # play(game_over,player_turn,board,how_many_players)
    else:
        return False
# ask to play again, then run intro()
def play_again():
    play_again_input = input("Play again? (Y or N)")
    if play_again_input == "Y" or play_again_input == "y":
        board = create_board()
        return intro()
    else:
        print("Thanks for the game.")
        # board = create_board()
        return False

# check winning orientations
def check_win(board):
#     # check horizontal for 4 across
    for r in board:
        for c in range(len(r)-3):
            if r[c] == 1 or r[c] == 2:
                if r[c] == r[c+1] == r[c+2] == r[c+3] :
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

    # negative diagonal
    for r in range(len(board)-3):
        for c in range(3, len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    print(print("Player ", str(board[r][c])[0]," wins!"))
                    return True
                  
# Check if top row is empty or full  
def is_valid_column(board,col):
    if int(board[0][col]) == 0:
        return True
    else:
        return False

# drop piece to bottom most available row in column
def drop_piece(board,col,player):
    if is_valid_column(board,col):
        for r in range(len(board)-1,-1,-1):
            if board[r][col] == 0:
                board[r][col] = player
                return True
    else:
        print("Column full. Please try another column.")
        return False

# drop computer piece until in valid column
def drop_piece_comp(board,col,player):
    if is_valid_column(board,col):
            for r in range(len(board)-1,-1,-1):
                if board[r][col] == 0:
                    board[r][col] = player
                    return True
    else:
        col = computer_player_move()
        drop_piece_comp(board,col,player)

# player inputs column
def input_column(board, player):
    player_input = 0
    while player_input >= 8 or player_input <= 0:
            # Handle input error if not an integer
            try:    
                player_input = int(input("Player "+str(player)+" Choose a column (1-7):"))
                # Check input between/including 1-7
                if player_input > 0 and player_input < 8:
                    player_input -= 1
                    if(drop_piece(board,player_input,player)):
                        print_board(board)
                        return True
                    else:
                        return False
                else:
                    print("Please input integer between 1-7")
            # on integer input error
            except:
                print("Please input integer between 1-7, inclusive")

# single or two player game logic
#  ##### bug present: on 2 player game re-do, always restarts game
def play(game_over,player_turn,board,how_many_players):
    print_board(board)
    while not game_over:
        if player_turn == 1:
            if input_column(board,1) == True:
                player_turn = 2
                if(check_win(board)):
                    if play_again():
                        play_again()
                    else:
                        break
            else:
                player_turn = 1

        if player_turn == 2:
            if how_many_players == 2:
                if input_column(board,2) == True:
                    player_turn = 1
                    if(check_win(board)):
                        if play_again():
                            play_again()
                        else:
                            break
                else:
                    player_turn = 2
            else:
                col = computer_player_move()
                if drop_piece_comp(board,col,player_turn):
                    print_board(board)
                    player_turn = 1
                    if(check_win(board)):
                        if play_again():
                            play_again()
                        else:
                            break
                    
                else:
                    player_turn = 2
    
# run two player game logic
def play_two_player(game_over,player_turn,board):
    print_board(board)
    while not game_over:
        if player_turn == 1:
            if input_column(board,1) == True:
                player_turn = 2
                if(check_win(board)):
                    play_again()
                    break

            else:
                player_turn = 1

        if player_turn == 2:
            if input_column(board,2) == True:
                player_turn = 1
                if(check_win(board)):
                    play_again()
                    break
            else:
                player_turn = 2
        
# run single player game logic
def play_one_player(game_over,player_turn,board):
    print_board(board)
    while not game_over:
       
        if player_turn == 1:
            if input_column(board,1) == True:
                player_turn = 2
                if(check_win(board)):
                    play_again()
                    break

            else:
                player_turn = 1

        if player_turn == 2:
            col = computer_player_move()
            if drop_piece_comp(board,col,player_turn):
                print_board(board)
                player_turn = 1
                if(check_win(board)):
                    play_again()
                    break
            else:
                player_turn = 2

# Play game
intro()


# IMPROVEMENTS TO BE MADE
# 1. re-factor game logic based on number of players so it is DRY
# 2. create option to start as player 1 or 2 in single player
# 3. make AI at least competitive
# 4. practice with classes. Save player profile to local memory as class object?
