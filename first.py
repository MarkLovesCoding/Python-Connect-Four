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



GAME_OVER = False
player_turn = 1
plays = {"Player 1":[],"Player 2":[]}

# def verify_input(input):

#     if type(input == int):
#         try:
#             if int(input) > 0 and int(input) <= 7:
#                 return input
#             else:
#                 print("Number not in range. Try another in range.")
#                 return 
#         except:
#             print("Errorrr")
#     # return print("Error")
    #  

def drop_piece(board,col,player):
    if is_space_available(board,col):
        for r in range(len(board)-1,-1,-1):
            if board[r][col] == 0:
                board[r][col] = player
                break
    else:
        print("Column full. Please try another column.")

def input_column(board, player):
    player_input = 0
    while player_input >= 8 or player_input <= 0:
        try:    
            player_input = int(input("Player "+str(player)+" Choose a column (1-7):"))
            # print(player_input)
            if player_input > 0 and player_input < 8:
                # print(player)
                player_input -= 1
                drop_piece(board,player_input,player)
                print(board)
                
            else:
              print("Please input integer between 1-7")
            

        
        except:
            print("Please input integer between 1-7, inclusive")

            
def is_space_available(board,col):
    for r in board:
            if r[col] == 0:
                return True
    return False



    # print("Please choose another column")


# drop_piece(board,1,1)
# drop_piece(board,1,2)
# drop_piece(board,1,3)
# drop_piece(board,1,4)
# drop_piece(board,1,5)
# drop_piece(board,1,6)
# drop_piece(board,1,7)
# print(board)

# print(board,is_space_available(board,2))

# def next_space_available():
#     pass
# def put_in_spot(col,board,player):
#     for i in board:



def play(GAME_OVER,player_turn,board):
    # print(create_board())
    while not GAME_OVER:
        # Get input for player 1
       
        if player_turn == 1:
            input_column(board,1)
            player_turn = 2

        if player_turn == 2:
            input_column(board,2)
            player_turn = 1

        

# print(print_board(board))
play(GAME_OVER,player_turn,board)
