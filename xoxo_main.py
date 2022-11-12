# Global variables

# game board
board=["-","-","-",
       "-","-","-",
       "-","-","-" ]

# if game is still going 
game_still_going=True

# game won or tie 
winner=None

# which players turn
current_player="X"

# display of the board
def display_board():
    print(board[0]+" | "+ board[1]+" | "+ board[2])
    print(board[3]+" | "+ board[4]+" | "+ board[5])
    print(board[6]+" | "+ board[7]+" | "+ board[8])

# main function for the game 
def play_game():
    
    
    display_board()

 # when game is going 
    while game_still_going:

        # handle the turn of player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #Flip to other player 
        flip_player() 
         
 # the game has ended
    if winner=="X" or winner=="O":
        print(winner+" won.")
    elif winner == None:
        print("TIE.")

# position of a player and input of position 
def handle_turn(player):

    print(player+"'s Turn.")
    position=input("Choose a position from 1-9: ")

    valid=False
    while not valid:

        while position not in["1","2","3","4","5","6","7","8","9"] :
            position = input("Invalid input Choose a position from 1-9: ")

        position=int(position) -1

        if board[position]=="-":
            valid=True
        else:    
            print("you cant go there. Go again.")

    board[position]=player

    display_board()

    
def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():

    # To set up global variables 
    global winner

    # check rows 
    row_winner=check_rows()
    #check columns 
    column_winner=check_columns()
    #check diagonals 
    diagonal_winner=check_diadonals()
    # get the winner 
    if row_winner:
        winner=row_winner      # there is a win 
    elif column_winner:
        winner=column_winner   # there is a win 
    elif diagonal_winner:
        winner=diagonal_winner # there is a win 
    else:
        # there is no winner 
        winner=None
    return



def check_rows():
    # set up of global var game_still_going =true
    global game_still_going
    # checking if the rows have the same value and not empty 
    row_1=board[0]==board[1]==board[2] !="-"
    row_2=board[3]==board[4]==board[5] !="-"
    row_3=board[6]==board[7]==board[8] !="-"
    # if any row has a match, then there is a win then game ends 
    if row_1 or row_2 or row_3:
        game_still_going=False
    # return the winner X or O 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]    
    return


def check_columns():
    # set up of global var game_still_going =true
    global game_still_going
    # checking if the rows have the same value and not empty 
    column_1=board[0]==board[3]==board[6] !="-"
    column_2=board[1]==board[4]==board[7] !="-"
    column_3=board[2]==board[5]==board[8] !="-"
    # if any diagonal has a match, then there is a win then game ends 
    if column_1 or column_2 or column_3:
        game_still_going=False
    # return the winner X or O 
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]    
    return


def check_diadonals():
    # set up of global var game_still_going =true
    global game_still_going
    # checking if the rows have the same value and not empty 
    diagonal_1=board[0]==board[4]==board[8] !="-"
    diagonal_2=board[6]==board[4]==board[2] !="-"
    # if any column has a match, then there is a win then game ends 
    if diagonal_1 or diagonal_2:
        game_still_going=False
    # return the winner X or O 
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]   
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return


def flip_player():
    # calling global variable current player to flip players 
    global current_player
    # if current player is X change it to O
    if current_player =="X":
        current_player="O"
    # if current player is O change it to X    
    elif current_player =="O":
        current_player="X"    
    return #flipping player to know whose turn it is   
play_game()