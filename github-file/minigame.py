import pygame
from pygame import mixer
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 255, 255)
yellow = (255, 255, 0)

# Initialize mixer for sound
pygame.mixer.init()

# Create game window
screen_width = 1000
screen_height = 900
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Burgery Snake")
pygame.display.update()

# Load images
background = pygame.image.load("water.png")
welcome_window = pygame.image.load("welcome.jpg")
over_window = pygame.image.load("GAMEOVER.png")
snakeimg = pygame.image.load("snake.png")
foodimg = pygame.image.load("hamburger.png")

# Set font for text
font = pygame.font.SysFont(None, 55)

# Function to display text on the screen
def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    game_window.blit(screen_text, [x, y])

# Function to plot the snake on the screen
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# Function to display snake image
def snake(x, y):
    game_window.blit(snakeimg, (x, y))

# Function to display food image
def food(x, y):
    game_window.blit(foodimg, (x, y))

# Set up the clock
Clock = pygame.time.Clock()

# Function to display the welcome screen
def game_welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(blue)
        game_window.blit(welcome_window, (0, 0))
        text_screen("Welcome to Burgy Snake!!", yellow, 250, 400)
        text_screen("Press Space to Play", yellow, 330, 450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.wav")
                    pygame.mixer.music.play(-1)
                    game_loop()

        pygame.display.update()
        Clock.tick(20)

# Main game loop
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 47
    snake_size = 40
    fps = 20
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))
    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            game_window.fill(white)
            game_window.blit(over_window, (0, 0))
            text_screen("Game Over! Press Enter to Continue", red, 200, 400)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("background.wav")
                        pygame.mixer.music.play(-1)
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
            
            snake_x += velocity_x
            snake_y += velocity_y

            # Check if snake eats the food
            if abs(snake_x - food_x) < 40 and abs(snake_y - food_y) < 40:
                score += 1
                print("Score:", score * 10)
                food_x = random.randint(20, int(screen_width / 2))
                food_y = random.randint(20, int(screen_height / 2))
                snake_length += 5

            game_window.fill(yellow)
            game_window.blit(background, (0, 0))
            text_screen("Score: " + str(score * 10), black, 5, 5)
            text_screen("Priyanka...", black, 830, 0)

            # Create snake head and add it to the snake list
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            # Check if snake collides with itself
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("explosion_with_tail.wav")
                pygame.mixer.music.play()

            # Check if snake collides with the boundaries
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("explosion_with_tail.wav")
                pygame.mixer.music.play()

            # Plot the snake and the food
            plot_snake(game_window, green, snake_list, snake_size)
            food(food_x, food_y)
            snake(snake_x, snake_y)

        pygame.display.update()
        Clock.tick(fps)

    pygame.quit()
    quit()

# Start the game by displaying the welcome screen
game_welcome()
