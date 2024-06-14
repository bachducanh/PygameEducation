import pygame
import time
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
window_width = 800
window_height = 600

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Tạo cửa sổ game
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Đồng hồ
clock = pygame.time.Clock()

# Kích thước mỗi ô vuông (mỗi đoạn của rắn)
block_size = 20
snake_speed = 15

# Font chữ cho điểm số
font_style = pygame.font.SysFont(None, 35)

def score_display(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    game_window.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, window_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, window_height - block_size) / block_size) * block_size

    score = 0

    direction = 'RIGHT'

    while not game_over:

        while game_close:
            game_window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    x1_change = -block_size
                    y1_change = 0
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    x1_change = block_size
                    y1_change = 0
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    y1_change = -block_size
                    x1_change = 0
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    y1_change = block_size
                    x1_change = 0
                    direction = 'DOWN'

        x1 += x1_change
        y1 += y1_change

        if x1 >= window_width:
            x1 = 0
        elif x1 < 0:
            x1 = window_width - block_size
        if y1 >= window_height:
            y1 = 0
        elif y1 < 0:
            y1 = window_height - block_size

        game_window.fill(white)
        pygame.draw.rect(game_window, green, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        score_display(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, window_height - block_size) / block_size) * block_size
            length_of_snake += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
