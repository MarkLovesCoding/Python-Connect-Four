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

def input_column(player, plays):
    player_input = 0
    while player_input >= 8 or player_input <= 0:
        try:
            if player_input <= 0 or player_input >=8:
                print("Please input integer between 1-7, inclusive")
            else:    
                player_input = int(input(player+" Choose a column (1-7):"))
                plays[player].append(player_input)
            
        except:
            print("Please input integer between 1-7, inclusive")

def is_space_available(board,col):
    for r in board:
            if r[col] == 0:
                return True
    return False
board[2][6]=2.6
board[5][1]=5.1
board[0][2]=0.2
print(board,is_space_available(board,2))

# def next_space_available():
#     pass
# def put_in_spot(col,board,player):
#     for i in board:



def play(GAME_OVER,player_turn,plays):
    print(create_board())
    while not GAME_OVER:
        # Get input for player 1
        if player_turn == 1:
            input_column("Player 1",plays)
            player_turn = 2

        if player_turn == 2:
            input_column("Player 2", plays)
            player_turn = 1

        if len(plays["Player 2"]) > 5:
            GAME_OVER = True
            print(plays)
            print("Game")


# print(print_board(board))
# play(GAME_OVER,player_turn,plays)
