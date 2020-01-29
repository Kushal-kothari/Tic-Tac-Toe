game_still_going = True #bool value
winner = None

current_player = "X"

board = ["-","-","-",
		 "-","-","-",
		 "-","-","-"] 
#this is a board where the game is going to be get played.Period.ok
def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2] )
	print(board[3] + " | " + board[4] + " | " + board[5] )
	print(board[6] + " | " + board[7] + " | " + board[8] )


def play_game():
	display_board()

	while game_still_going:

		handle_turn(current_player)

		check_if_game_over()

		flip_player()

	#if the game is going to get ended
	if winner == "X" or winner == "O":
		print(winner + " won.")	
	elif winner == None:
		print(" Tie.")	

def handle_turn(player):
	print(player + "'s turn.")
	position = input("Choose a position from 1-9: " )

	valid = False
	while not valid:

		while position not in ["1","2","3","4","5","6","7","8","9"]:
			position = input("Choose a position from 1-9: " )


		position = int(position) - 1

		if board[position] == "-":
			valid = True
		else :
			print("you cant go there.go again.") 

	board[position]= player
	display_board()

def check_if_game_over():
	check_for_winner()
	check_if_tie()



def check_for_winner():

	global winner

	#check rows
	row_winner = check_rows()
	#check columns
	column_winner = check_columns()
	#check diagonals
	diagonal_winner = check_diagonals()

	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else :
		#there was no winner
		winner=None		
	return

def check_rows():
	 # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None

def check_columns(): 
 # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None

def check_if_tie():
	global game_still_going
	if "-" not in board:
		game_still_going = False
	return


def flip_player():
	global current_player
	if current_player == "X":
		current_player = "O"

	elif current_player == "O":
		current_player = "X"	
		
	return	

play_game()







#board
#display the board
#play game
#flip between players
#check win
	#rows
	#columns
	#diagonals
#check tie

