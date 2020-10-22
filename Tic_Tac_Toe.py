# Importing the libraries
import pygame as pg
import sys
import time
from pygame.locals import*

# Making the global variables


# For storing X(cross) and O(circle)
XO = 'x'

# Storing the winner's value at any instance of code
winner = None

# To check if the game is draw
draw = None

# To set the width and the heihr of the window
width = 400
height = 400

# To set the background color of the game window
white = (255,255,255)

# Color of the straightlines on the white game board, dividing game into nine parts
line_color = (0,0,0)

# Setting 3 X 3 board in canvas, where user play the game
board = [None]*3,[None]*3,[None]*3







# Intialising the game window
pg.init()

# Setting FPS for game(manually)
fps = 30

# To track the time
CLOCK = pg.time.Clock()




# To build infarstructure of the game
screen = pg.display.set_mode((width,height+100),0,32)

# Title for the game window
pg.display.set_caption("Tic Tac Toe")

# Loading images in the game window(GUI)
initiating_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
o_img = pg.image.load("o_modified.png")

# Resizing images
initiating_window = pg.transform.scale(initiating_window,(width,height + 100))
x_img = pg.transform.scale(x_img,(80,80))
o_img = pg.transform.scale(o_img,(80,80))




def game_initiating_window():

    # Displaying over the screen
    screen.blit(initiating_window,(0,0))

    # Updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # Drawing vertcal lines
    pg.draw.line(screen,line_color,(width / 3,0),(width / 3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)

def draw_status():

    # Getting the global variable draw into action
    global draw

    if winner is None:
        message = XO.upper()+"s Turn"
    else:
        message = winner.upper()+"won!"
    if draw:
        message = "Game Draw!"

    # Setting a font object
    font = pg.font.Font(None,30)

    # Setting font properties
    text = font.render(message,1,(255,255,255))

    # Display the render message on the board
    screen.fill((0,0,0),(0,400,500,100))
    text_rect = text.get_rect(center = (width/2,500-50))
    screen.blit(text,text_rect)
    pg.display.update()

def check_win():
    global board, winner, draw

    # Checking the winning rows
    for row in range(0,3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):

            winner = board[row][0]
            pg.draw.line(screen,(250,0,0),
            (0,(row + 1)*height/3-height / 6),
            (width,(row+1)*height/3-height/6),
            4)

        break
    # Checking for winning columns
    for col in range(0,3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen,(250,0,0),((col + 1)* width/3-width/6,0),\
                ((col + 1)* width/3-width/6,height),4)
            break
    
    # Checking for winning columns
    for col in range(0,3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen,(250,0,0),((col+1)*width/3 - width/6,0),\
                ((col+1)*width/3-width/6,height),4)
            break

    # Checking for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        # Left to right
        winner = board[0][0]
        pg.draw.line(screen,(250,70,70),(50,50),(350,350),4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

        # Right to left
        winner = board[0][2]
        pg.draw.line(screen,(250,70,70),(350,50,),(50,350),4)

    if(all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()

def drawXO(row,col):
    global board, XO

    # iamge for first row
    if row == 1:
        posx = 30

    # Image for the second row
    if row == 2:
        posx = width / 3 +30

    if row == 3:
        posx = width/3 * 2 + 30
         
    # Image for the first column
    if col == 1:
        posy = 30

    if col == 2:
        posy = height / 3 + 30

    if col == 3:
        posy = height/3*2 + 30

    # Setting up the board

    board[row-1][col-1] == XO

    if (XO == 'x'):
        screen.blit(x_img,(posy,posx))
        XO = 'o'

    else:
        screen.blit(o_img,(posy,posx))
        XO ='x'

    pg.display.update()

def user_click():
    # Coordinates of mouse

    x,y = pg.mouse.get_pos()

    # Get columns of mouse
    if(x<width/3):
        col = 1

    elif (x<width/3*2):
        col = 2

    elif (x<width):
        col = 3

    else:
        col = None

    # Get row of mouse click

    if(y<height/3):
        row = 1

    elif (y<height/3*2):
        row = 2

    elif (y<height):
        row = 3

    else:
        row = None


    # Draw images at required position
    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row,col)
        check_win()


def reset_game():
    global board, winner, XO,draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3,[None]*3,[None]*3]

game_initiating_window()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            user_click()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)

            
