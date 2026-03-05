import sys, pygame, random
#import pygame + sys libraries, and randrange function from random library

#initialize pygame
pygame.init()

#make color variables
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(180, 0, 0)
purple = pygame.Color(180, 0, 180)
blue = pygame.Color(0, 0, 180)

#create a window and set its size + background color
window_size = width, height = 500, 500
window = pygame.display.set_mode(window_size) 
window.fill(black) #set background color as black (color value stored in bg_color) 
pygame.display.set_caption(f'Snake  (score: 0)')

#create 20x20 grid to fill window, and set cell sizes
ROWS = 20
COLUMNS = 20
cell_width = width // COLUMNS
cell_height = height // ROWS

#track game speed
fps = pygame.time.Clock()
#initialize frame count, score, snake speed,
score = 0
snake_speed = 6
frame_count = 0

#define  starting snake coords & direction
snake_body = [[100, 50], [75, 50], [50, 50]]
direction = (25, 0)

#main game loop
def main():
    global direction, score, frame_count #allow modification of global variables

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit() #quit cleanly if window is closed
        
        #set direction when pressing movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 25):
                direction = (0, -25)
            elif event.key == pygame.K_DOWN and direction != (0, -25):
                direction = (0, 25)
            elif event.key == pygame.K_LEFT and direction != (25, 0):
                direction = (-25, 0)
            elif event.key == pygame.K_RIGHT and direction != (-25, 0):
                direction = (25, 0)

        #snake redrawing logic
        if frame_count % snake_speed == 0:
            new_head = [snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]] #calculate the new head position
            snake_body.insert(0, new_head) #add the new head to the body 
            snake_body.pop() #remove the tail to maintain length

        window.fill(black) #reset background to black 
        for segment in snake_body:    
            pygame.draw.rect(window, purple, pygame.Rect(segment[0], segment[1], cell_height, cell_width)) #draw new snake

        pygame.display.flip() #refresh the screen to show the snake
        fps.tick(60) #maintain snake speed based on fps
        frame_count += 1 #increment frame
        pygame.display.set_caption(f'Snake  (score: {score})') #refresh window caption


#displays game over screen and ask to play again or quit
def gameover():
    #initialize font
    font = pygame.font.SysFont('arial', 80)

    #initialize game over and retry message surfaces for text
    game_over_surface = font.render(f'Your Score is : {score}')

    #initialize rect objects for game over message positioning
    game_over_rect = game_over_surface.get_rect()

    #set display coords for game over message
    game_over_rect.midtop(width/2, height/3)

    #display game over message
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000) #wait 3 seconds

    #quit pygame library
    pygame.quit()
    
    # quit the program
    quit()

#call main
if __name__ == "__main__":
    main()