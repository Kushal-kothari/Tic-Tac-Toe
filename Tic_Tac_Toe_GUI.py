# This is a GUI version of the TIC-TAC-TOE game.
# It has used the 'finaltictactoe.py' as a library and used its function to create the game.
#vxv

import pygame
import finaltictactoe as game

pygame.init()


#can edit dimensions to change window frame
SCREEN_WIDTH  = 255
SCREEN_HEIGHT = 255

#Create and initialize pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
size = int(len(game.brd)**(1/2))
width = SCREEN_WIDTH//size

#Create font style to dsiplay text on screen
font = pygame.font.Font('freesansbold.ttf', 32)


#Function to display text on screen
def show_result(text) :
    '''
    This function takes a string as an input and displays it on the screen
    '''
    text = font.render(text, True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    screen.blit(text, textRect)

#showing grid screen design with width and ondsiplay change
def show_board() :
    '''
    Display function to show the game board and game state on the screen
    '''
    #Draw the grid for the game
    for x in range (size) :
        pygame.draw.line(screen, (0,0,0), (x*width, 0), (x*width, SCREEN_HEIGHT))
        pygame.draw.line(screen, (0,0,0), (0, x*width), (SCREEN_WIDTH, x*width))
    
    #Draw the player moves on the screen
    for x in range (size) :
        for y in range (size) :
            pos = size*x + y
            #If the move is a X, draw an X on the particular grid block
            if (game.brd[pos] == 'X') :
                a = (y*width) + (width//4)
                b = (y*width) + ((3*width)//4)
                c = (x*width) + (width//4)
                d = (x*width) + ((3*width)//4)
                pygame.draw.line(screen, (0,0,0), (a,c), (b,d), 4)
                pygame.draw.line(screen, (0,0,0), (b,c), (a,d), 4)
            #If the move is a O, draw a O on the particular grid block
            if (game.brd[pos] == 'O') :
                x1 = (y*width) + (width//2)
                y1 = (x*width) + (width//2)
                pygame.draw.circle(screen, (0,0,0), (x1, y1), width//4, 4)

game_over = False
running = True
while running :

    screen.fill((255,255,255))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        #If a position is clicked on then find the coordinates and draw that move on the particular position
        if event.type == pygame.MOUSEBUTTONDOWN : 
            if pygame.mouse.get_pressed()[0] :
                if not game_over :
                    pos = pygame.mouse.get_pos()
                    block = str(((pos[0]//width))+((pos[1]//width)*size)+1)
                    game.handle_turn(game.cur_player,block)
                    game.flip_player()
        
    game.check_if_game_over()
    #If the game has ended then show the result on the screen
    if game.winner == "X" or game.winner == "O":
        show_result(game.winner + " won.")
        game_over = True
    elif game.game_still_going == False:
        show_result(" Tie. ")	
        game_over = True
    #If the game has not ended then show the game board and continue play
    else :
        show_board()
    pygame.display.update()
//com
