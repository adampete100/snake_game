import sys, pygame, random
#import pygame + sys libraries, and randrange function from random library

#initialize pygame
pygame.init()

#make color variables to utilize for background, snake, and fruit color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(180, 0, 0)
purple = pygame.Color(180, 0, 180)
cyan = pygame.Color(0, 190, 230)

#set window dimensions and cell size (was originally a percentage of the dimension, 
#this new setup makes it the same regardless of window dimensions)
window_size = window_width, window_height = 800, 600
CELL_SIZE = 25
cell_width = CELL_SIZE
cell_height = CELL_SIZE

window = pygame.display.set_mode(window_size) 
window.fill(black) #set background color as black
pygame.display.set_caption(f'Snake  (score: 0)')

#make a grid for the snake and fruit to be drawn on
ROWS = 20
COLUMNS = 20

#track game speed
fps = pygame.time.Clock()
#initialize frame count, score, snake speed,
score = 0
snake_speed = 6
frame_count = 0

#define starting snake coords & direction
snake_body = [[100, 50], [75, 50], [50, 50]]
direction = (CELL_SIZE, 0)

#picks a random grid-aligned spot within the window, and spawns a fruit there
def spawn_fruit():
    while True:
       #subtract CELL_SIZE from width/height so fruit doesn't spawn off-screen
        x = random.randrange(0, window_width - CELL_SIZE, CELL_SIZE)
        y = random.randrange(0, window_height - CELL_SIZE, CELL_SIZE)
        fruit = [x, y]
        #check if fruit coordinates are within the snake coordinates.
        if fruit not in snake_body:
            return fruit
        #if they are, the while loop runs again until they are outside of the snake body

#initialize the fruit coordinates for later
fruit_coords = spawn_fruit()

#main game loop
def main():
    global direction, score, frame_count, fruit_coords #allow modification of global variables
    direction_changed = False #tracks if the snake has turned in a given tick

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit() #quit cleanly if window is closed

            #check for key pressess, and set direction coorelated to the movement keys
            #also uses the direction_changed variable to only allow one direction per movement cycle
            if event.type == pygame.KEYDOWN and not direction_changed:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                    direction_changed = True
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                    direction_changed = True
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                    direction_changed = True
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
                    direction_changed = True

        #redraw snake with new head position after moving it in the player's input direction 
        #(happens every 6 frames out of 60 (10 times in a second))
        #also, resets the direction_changed variable for the next movement cycle
        if frame_count % snake_speed == 0:
            direction_changed = False
            new_head = [snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]] #calculate the new head position

            #check if the new head overlaps with the body (collides with it), and end the game if it does
            if new_head in snake_body:
                is_high_score = save_high_score() #if there is a new high score, it'll return true here
                gameover(is_high_score)

            #check if the new head goes outside the bounds of the window, and end the game if it does
            if (new_head[0] < 0 or new_head[0] >= window_width or 
                new_head[1] < 0 or new_head[1] >= window_height):
                is_high_score = save_high_score()
                gameover(is_high_score)

            snake_body.insert(0, new_head) #add the new head to the body 
                
            if fruit_coords == new_head:
                score += 1 #adds to displayed score variable on window caption
                fruit_coords = spawn_fruit()
            else: 
                snake_body.pop() #remove the tail to maintain length (if fruit wasn't eaten)
                
        window.fill(black) #reset background to black 
        #(this makes the redraw exclude the extra tail leftover from previous snake position, otherwise it'd remain onscreen)
        print(f"DEBUG: fruit_coords is {fruit_coords}")
        pygame.draw.rect(window, red, pygame.Rect(fruit_coords[0], fruit_coords[1], CELL_SIZE, CELL_SIZE)) #draw fruit
        for segment in snake_body:    
            pygame.draw.rect(window, purple, pygame.Rect(segment[0], segment[1], cell_height, cell_width)) #draw new snake

        pygame.display.flip() #refresh the screen to show the new snake
        fps.tick(60) #set fps
        frame_count += 1 #increment frame count
        pygame.display.set_caption(f'Snake  (score: {score})') #refresh window caption


#display game over screen and displays the highscore and "press key to quit" messages. 
#quits in the event of a keypress or when the window closes
def gameover(is_high_score):
    
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
    
    #render disctinct fonts for different messages
    title_font = pygame.font.SysFont('arial', 80)
    info_font  = pygame.font.SysFont('arial', 30)
    high_score_font = pygame.font.SysFont('comic sans', 20)

    #render surface text with a set font variable, and pick a color for the text
    title_surface = title_font.render('GAME OVER', True, white)
    score_surface = info_font.render(f'Final Score: {score}', True, white)
    quit_surface  = info_font.render('Press any key to Quit', True, white)
    high_score_surface = high_score_font.render(f'High Score: {high_score}', True, white)
    new_high_score_surface = high_score_font.render(f'New High Score!', True, cyan)

    #set surface coords relative to screen center
    high_score_rect = high_score_surface.get_rect(center=(window_width/2, window_height/5))
    new_high_score_rect = new_high_score_surface.get_rect(center=(window_width/2, window_height/7))
    title_rect = title_surface.get_rect(center=(window_width/2, window_height/3))
    score_rect = score_surface.get_rect(center=(window_width/2, window_height/2))
    quit_rect  = quit_surface.get_rect(center=(window_width/2, window_height/1.5))
    


    #place message surfaces and refresh screen to display them 
    window.blit(new_high_score_surface, new_high_score_rect)
    if is_high_score: #checks if there's a new high score (a True bool wuold be stored if so), 
                   #and displays the high score message if there is
        window.blit(high_score_surface, high_score_rect)
    window.blit(title_surface, title_rect)
    window.blit(score_surface, score_rect)
    window.blit(quit_surface, quit_rect)
    pygame.display.flip()


    
    #checks for either user input or the window to get closed, then closes the program after 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

#saves the high score in a text file
def save_high_score():

    #checks if high score file exists yet, if not the high score becomes zero temporarily
    try:
        with open("high_score.txt", "r") as file:
            current_high_score = int(file.read())
    except (FileNotFoundError, ValueError):
        current_high_score = 0

    #check if high score is lower than the current score, and updates it if it is 
    #(if there is no high score yet, it's set to zero for now, so it'll write a new high score)
    if current_high_score < score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))
        return True
    


#call main to run the program
if __name__ == "__main__":
    main()