# Importing pygame module
import pygame
from pygame.locals import *
import Domineering 


# TODO: winner check, valid move check, numbers and letters

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
Domineering.initialize(8, 8, Domineering.HUMAN)

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((800, 800))

# Fill the scree with white color
window.fill((255, 255, 255))


SIZE = 80
is_black = False
m, n = 8, 8
OFFSET = 50
for i in range(m):
    is_black = not is_black
    for j in range(n):
        pygame.draw.rect(window, (153, 153, 153) if is_black else (
            255, 255, 255), [OFFSET+i*SIZE, OFFSET+j*SIZE, SIZE, SIZE])
        is_black = not is_black

scale_x, scale_y = 2, 1
color1, color2 = (211, 100, 59), (64, 59, 51)

# Creating a variable which we will use
# to run the while loop
run = True

# Creating a while loop
while run:

    # Iterating over all the events received from
    # pygame.event.get()
    for event in pygame.event.get():

        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == QUIT:
            run = False

        # if the type of the event is MOUSEBUTTONDOWN
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            if Domineering.play_move((position[0]-OFFSET)//SIZE, (position[1]-OFFSET)//SIZE):
                pygame.draw.rect(window, color1, [
                                ((position[0]-OFFSET)//SIZE)*SIZE+5+OFFSET, ((position[1]-OFFSET)//SIZE-scale_x+1)*SIZE+5+OFFSET, SIZE*scale_y-10, SIZE*scale_x-10], 0, 10)
                pygame.draw.rect(window, (0, 0, 0), [
                                ((position[0]-OFFSET)//SIZE)*SIZE+5+OFFSET, ((position[1]-OFFSET)//SIZE-scale_x+1)*SIZE+5+OFFSET, SIZE*scale_y-10, SIZE*scale_x-10], 2, 10)
                scale_x, scale_y = scale_y, scale_x
                color1, color2 = color2, color1
                Domineering.print_board()
                win = Domineering.check_winner()
                if win != "N":
                    print("\n")
                    print("Winner is " + win)
                
                next_state = Domineering.minmax(Domineering.board, 3, True)
                Domineering.print_board()
                Domineering.board = next_state[0]
                move=next_state[2]
                pygame.draw.rect(window, color1, [
                            (move[1])*SIZE+5+OFFSET, (move[0]-scale_x+1)*SIZE+5+OFFSET, SIZE*scale_y-10, SIZE*scale_x-10], 0, 10)
                pygame.draw.rect(window, (0, 0, 0), [
                            (move[1])*SIZE+5+OFFSET, (move[0]-scale_x+1)*SIZE+5+OFFSET, SIZE*scale_y-10, SIZE*scale_x-10], 2, 10)
                scale_x, scale_y = scale_y, scale_x
                color1, color2 = color2, color1
                Domineering.next += 1
                win = Domineering.check_winner()
                if win != "N":
                    print("\n")
                    print("Winner is " + win)

    # Draws the surface object to the screen.
    pygame.display.update()
