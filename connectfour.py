import numpy
import random
import operator
# INITIALIZE ROWS/COLUMNS VARS
ROWS = 6
COLUMNS = 7

def create_board():
    board = numpy.zeros((ROWS,COLUMNS))
    return board

test_board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,1,2],
        [1,1,1,0,2,2,2],
        [2,2,2,0,1,1,1],
        [2,1,1,2,2,1,1]]
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

##
## AI Tester
##
def check_vertical_score(board,col,row):
    score = 0
    available_top = 5 - row
    if row < 4:
        one_below = board[row + 1][col]
    if row < 3:
        two_below = board[row + 2][col]
    if row < 2:
        three_below = board[row + 3[col]
    print("one to three: {0}, {1}, {2}".format(one_below,two_below,three_below))
    if three_below == 2 and two_below == 2 and one_below == 2:
        if available_top >= 1:
            score = 30 + available_top
    elif two_below == 2 and one_below == 2:
        if available_top >= 2:
            score = 20 + available_top
    elif one_below == 2:
        if available_top >= 3:
            score = 10 + available_top
    elif one_below !=2:
        if available_top >=4:
            score = available_top
    else:
        score = available_top
    return score



def check_horizontal_score(board,col,row):
    available_right = 3 if col <=3 else 6 - col
    available_left = 3 if col >=3 else col
    # available = [available_left,available_right]
    # print("Available Left: {0} \nAvailable Right:{1}".format(available_left,available_right))
    score = 0
    temp_left = available_left
    temp_right = available_right
    # print(temp_right,temp_left)
    if temp_left >= 0:
        while temp_left > 0:
            # print(board[row][col - temp_left])

            if board[row][col - temp_left] == 0:
                score += 1
            if board[row][col - temp_left] == 2:
                score += 10
            temp_left -= 1
    if temp_right >= 0:
        while temp_right > 0:
            # print(board[row][col - temp_right])

            if board[row][col + temp_right] == 0:
                score += 1
            if board[row][col + temp_right] == 2:
                score += 10
            temp_right -= 1    
    return score
    
                
score = {}
def ai_score(board, col,row):
    # score = {}

    score[col] = check_horizontal_score(board,col,row) + check_vertical_score(board,col,row)
    print(score)
        
    return max(score.items(), key=operator.itemgetter(1))[0]
    # ,check_vertical_score(col) ,check_pos_diagonal_score(col) ,check_neg_diagonal_score(col,row))
    

def computer_choose_column_smart(board):
    # available_cols = []
    best_col = None
    for col in range(len(board[0])):
        if is_valid_column(board,col):
            for row in range(len(board)-1,-1,-1):
                if board[row][col] == 0:
                    # print(test_board)
                    # print(col, row)
                            
                    # print(ai_score(board,col,row))
                    if (best_col is None) or (ai_score(board,col,row) > best_col):
                        best_col = ai_score(board,col,row)
                    break
                    # check_horizontal(boa

    print("Best Col: {0}".format(best_col))
    return best_col




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
    elif how_many != "2" or how_many != 2 or how_many != "1" or how_many != 1:
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
    for r in range(0,len(board) - 3):
        for c in range(0,len(board[r]) - 3):
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
        col = computer_choose_column_smart(board)
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
                col = computer_choose_column_smart(board)
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
            # computer_choose_column_smart(board)

            col = computer_choose_column_smart(board)
            if drop_piece_comp(board,col,player_turn):
                print_board(board)
                player_turn = 1
                if(check_win(board)):
                    play_again()
                    break
            else:
                player_turn = 2

# def ai(player_count):
# computer_choose_column_smart(test_board)
# Play game
intro()