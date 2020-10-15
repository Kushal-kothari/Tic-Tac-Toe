game_still_going = True
	winner = None
	
	cur_player = "X"
	
	brd = ["-","-","-",
			 "-","-","-",
			 "-","-","-"] 
	#this is a brd where the game is going to be get played.Period.ok
	def show_brd():
		print(brd[0] + " | " + brd[1] + " | " + brd[2] )
		print(brd[3] + " | " + brd[4] + " | " + brd[5] )
		print(brd[6] + " | " + brd[7] + " | " + brd[8] )
	
	
	def play_game():
		show_brd()
	
		while game_still_going:
	
			handle_turn(cur_player)
	
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
	
			while position not in ["1","2","3","4","4","6","7","8","9"]:
				position = input("Choose a position from 1-9: " )
	
	
			position = int(position) - 1
	
			if brd[position] == "-":
				valid = True
			else :
				print("you cant go there.go again.") 
	
		brd[position]= player
		show_brd()
	
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
	  row_1 = brd[0] == brd[1] == brd[2] != "-"
	  row_2 = brd[3] == brd[4] == brd[5] != "-"
	  row_3 = brd[6] == brd[7] == brd[8] != "-"
	  # If any row does have a match, flag that there is a win
	  if row_1 or row_2 or row_3:
	    game_still_going = False
	  # Return the winner
	  if row_1:
	    return brd[0] 
	  elif row_2:
	    return brd[3] 
	  elif row_3:
	    return brd[6] 
	  # Or return None if there was no winner
	  else:
	    return None
	
	def check_columns(): 
	 # Set global variables
	  global game_still_going
	  # Check if any of the columns have all the same value (and is not empty)
	  column_1 = brd[0] == brd[3] == brd[6] != "-"
	  column_2 = brd[1] == brd[4] == brd[7] != "-"
	  column_3 = brd[2] == brd[5] == brd[8] != "-"
	  # If any row does have a match, flag that there is a win
	  if column_1 or column_2 or column_3:
	    game_still_going = False
	  # Return the winner
	  if column_1:
	    return brd[0] 
	  elif column_2:
	    return brd[1] 
	  elif column_3:
	    return brd[2] 
	  # Or return None if there was no winner
	  else:
	    return None
	
	
	# Check the diagonals for a win
	def check_diagonals():
	  # Set global variables
	  global game_still_going
	  # Check if any of the columns have all the same value (and is not empty)
	  diagonal_1 = brd[0] == brd[4] == brd[8] != "-"
	  diagonal_2 = brd[2] == brd[4] == brd[6] != "-"
	  # If any row does have a match, flag that there is a win
	  if diagonal_1 or diagonal_2:
	    game_still_going = False
	  # Return the winner
	  if diagonal_1:
	    return brd[0] 
	  elif diagonal_2:
	    return brd[2]
	  # Or return None if there was no winner
	  else:
	    return None
	
	def check_if_tie():
		global game_still_going
		if "-" not in brd:
			game_still_going = False
		return
	
	
	def flip_player():
		global cur_player
		if cur_player == "X":
			cur_player = "O"
	
		elif cur_player == "O":
			cur_player = "X"	
			
		return	
	
	play_game()
	
	
	
	
	
	
	
	#brd
	#show the brd
	#play game
	#flip between players
	#check win
		#rows
		#columns
		#diagonals
	#check tie

