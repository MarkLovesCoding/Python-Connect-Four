import numpy
import random
import operator
import math
import pygame
import sys
# INITIALIZE ROWS/COLUMNS VARS
ROWS = 6
COLUMNS = 7
PLAYER_PIECE = 1
COMP_PIECE = 2
EMPTY_PIECE = 0
WINDOW_LENGTH = 4

# PYGAME
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()

SQUARESIZE = 100

width = COLUMNS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width,height)

RADIUS = int(SQUARESIZE/2 -5)

screen = pygame.display.set_mode(size)
def draw_board(board):
	for c in range(COLUMNS):
		for r in range(ROWS):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMNS):
		for r in range(ROWS):		
			if board[r][c] == PLAYER_PIECE:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == COMP_PIECE: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

def create_board():
    board = numpy.zeros((ROWS,COLUMNS))
    return board

test_board = [
        [0,0,0,0,0,2,0],
        [0,0,0,0,0,1,0],
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

    print(numpy.flip(board,0))
    print("  1  2  3  4  5  6  7  ")

# random column for computer move (basic easy 1 player game)
# def computer_player_move():
#     column = random.randint(0,6)
#     return column

##
## AI Tester
##
# print(test_board[3,:])

def eval_window(window,player):
    score = 0
    opp_player = PLAYER_PIECE
    if player == PLAYER_PIECE:
        opp_player = COMP_PIECE

    if window.count(player) == 4:
        score += 100
    if window.count(player) == 3 and window.count(EMPTY_PIECE) == 1:
        score += 5
    if window.count(player) == 2 and window.count(EMPTY_PIECE) == 2:
        score += 2
    # CHECK IF PLAYER 1 WINS, BLOCK
    if window.count(opp_player) == 3 and (window.count(EMPTY_PIECE)):
        score -= 4    
    # if window.count(opp_player) == 3 and (window.count(player)):
    #     score += 100
    return score

def score_at_position(board, player):

    opp_player = PLAYER_PIECE
    if player == PLAYER_PIECE:
        opp_player = COMP_PIECE

    score = 0
    # Check Center position
    center_arr = [int(i) for i in list(board[:,COLUMNS // 2])]
    center_count = center_arr.count(player)
    score += center_count * 3

    # Check Horizontal score
    for r in range(ROWS):
        row_arr = [i for i in list(board[r,:])]
        for col in range(COLUMNS - 3):
            window = row_arr[col:col + 4]
            score += eval_window(window,player)
            # CHECK IF PLAYER 1 WINS, BLOCK

    # Check vertical score             
    for c in range(COLUMNS):
        col_arr = [i for i in list(board[:,c])]
        for r in range(ROWS - 3):
            window = col_arr[r:r + 4]
            score += eval_window(window,player)

    # Check diagonal up-left
    for r in range(ROWS - 3):
        # diag_pos_arr = [i for i in list(board[:,c])]
        for c in range(COLUMNS - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += eval_window(window,player)

    # Check diagonal up-right
    for r in range(ROWS - 3):
        # diag_pos_arr = [i for i in list(board[:,c])]
        for c in range(3, COLUMNS):
            window = [board[r + i][c - i] for i in range(4)]
            score += eval_window(window,player)


    return score


def is_terminal_node(board):
    return check_win(board, PLAYER_PIECE) or check_win(board, COMP_PIECE) or len(get_valid_columns(board)) == 0

# MINIMAX implimentation with alpha, beta params. 
def minimax(board, depth, alpha, beta, maximizing_player):
    valid_locations = get_valid_columns(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, COMP_PIECE):
                return(None, 1000000000)
            elif check_win(board, PLAYER_PIECE):
                return(None, -1000000000)
            else:
                return(None, 0)
        else:
            return (None, score_at_position(board,COMP_PIECE))
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            board_copy = board.copy()
            drop_piece(board_copy,row,col,COMP_PIECE)
            new_score = minimax(board_copy,depth - 1, alpha, beta, False)
            if new_score[1] > value:
                value = new_score[1]
                column = col
            alpha = max(alpha, value)
            if alpha > beta:
                break
        return column, value
    # minimizing player
    else: 
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            board_copy = board.copy()
            drop_piece(board_copy,row,col,PLAYER_PIECE)
            new_score = minimax(board_copy,depth - 1, alpha, beta, True)
            if new_score[1] < value:
                value = new_score[1]
                column = col
            beta = min(beta, value)
            if alpha > beta:
                break
        return column, value


def get_valid_columns(board):
    valid_columns = []
    for col in range(COLUMNS):
        if is_valid_column(board,col):
            valid_columns.append(col)
    return valid_columns
        

def choose_best_move(board, player):
    best_score = 0
    valid_columns = get_valid_columns(board)
    best_col = random.choice(valid_columns)
    for col in valid_columns:
        score = 0
        # row = get_open_row(board, col)
        temp_board = board.copy()
        row = get_open_row(board, col)
        drop_piece(temp_board, row, col, player)
        score = score_at_position(temp_board, player)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col

# def computer_choose_column_smart(board):

# standard starting
# how_many = 2
how_many_players = 2
# play game
def intro():
    
    
    
    board = create_board()


    # how_many = input(intro_banner)
    how_many = 1
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
def check_win(board, piece):
    opp_piece = 1
    if piece == 1:
        opp_piece = 2

#     # check horizontal for 4 across
    for r in board:
        for c in range(len(r)-3):
            if r[c] == piece or r[c] == opp_piece:
                if r[c] == r[c+1] == r[c+2] == r[c+3] :
                    # print("Player ", str(r[c])[0]," wins!")
                    return True
    # vertical check
    for r in range(len(board) - 3):
        for c in range(len(board[r])):
            if board[r][c] == piece or board[r][c] == opp_piece:
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    # print("Player ", str(board[r][c])[0]," wins!")
                    return True
    # positive diagonal
    for r in range(0,len(board) - 3):
        for c in range(0,len(board[r]) - 3):
            if board[r][c] == piece or board[r][c] == opp_piece:
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    # print("Player ", str(board[r][c])[0]," wins!")
                    return True

    # negative diagonal
    for r in range(len(board)-3):
        for c in range(3, len(board[r])):
            if board[r][c] == piece or board[r][c] == opp_piece:
                if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    # print(print("Player ", str(board[r][c])[0]," wins!"))
                    return True
                  
# Check if top row is empty or full  
def is_valid_column(board,col):
    # print(board[ROWS - 1][col])
    if board[ROWS - 1][col].any() == 0:
        return True
    else:
        return False


def get_open_row(board,col):
    if is_valid_column(board,col):
        for r in range(ROWS):
            if board[r][col] == 0:
                return r
    else:
        print("No open row")
        return None


# drop piece to bottom most available row in column
def drop_piece(board,row,col,player):

        board[row][col] = player

 

                    

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
                    row = get_open_row(board, player_input)
                    if row != None:
                        drop_piece(board,row,player_input,player)
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


   
    player_turn = random.randint(PLAYER_PIECE,COMP_PIECE)
    draw_board(board)


    print_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace",75)

    while not game_over:
        


        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                sys.exit()
                

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
                posx = event.pos[0]
                if player_turn == PLAYER_PIECE:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)),RADIUS)
                    if player_turn == COMP_PIECE:
                
                        col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)
                        # col = choose_best_move(board,player_turn)
                        row = get_open_row(board,col)
                        if row != None:
                            drop_piece(board,row,col, player_turn)
                            # print_board(board)
                            player_turn = 1
                            if(check_win(board, player_turn)):
                                label = myfont.render("Player 2 wins", 1, YELLOW)
                                screen.blit(label,(40,10))
                                game_over = True
                                # print("Computer player wins!")

                                # if play_again():
                                #     play_again()
                                # else:
                                    
                            print_board(board)
                            draw_board(board)
                        else:
                            player_turn = 2
                    if game_over:
                        pygame.time.wait(3000)       
                        intro()
                pygame.display.update()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))


                if player_turn == PLAYER_PIECE:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if is_valid_column(board,col):
                        row = get_open_row(board,col)
                        drop_piece(board,row,col,PLAYER_PIECE)
                        player_turn = 2
                        if(check_win(board, PLAYER_PIECE)):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            # print("You won!")
                            screen.blit(label,(40,10))
                            game_over = True
                            # if play_again():
                            #     play_again()
                            # else:
                            #     break
                    else:
                        player_turn = 1

                    print_board(board)
                    draw_board(board)
                if player_turn == COMP_PIECE:
                
                    col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)
                    # col = choose_best_move(board,player_turn)
                    row = get_open_row(board,col)
                    if row != None:
                        drop_piece(board,row,col, player_turn)
                        # print_board(board)
                        player_turn = 1
                        if(check_win(board, player_turn)):
                            label = myfont.render("Player 2 wins", 1, YELLOW)
                            screen.blit(label,(40,10))
                            game_over = True
                            # print("Computer player wins!")

                            # if play_again():
                            #     play_again()
                            # else:
                                
                        print_board(board)
                        draw_board(board)
                    else:
                        player_turn = 2
                if game_over:
                    pygame.time.wait(3000)       
                    intro()
# Play game
intro()
