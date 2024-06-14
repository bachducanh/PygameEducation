import pygame
import random

pygame.init()

# Kích thước cửa sổ game
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Brick Breaker')

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Đồng hồ
clock = pygame.time.Clock()
ball_speed = [4, -4]
paddle_speed = 10

# Tọa độ và kích thước của thanh ngang
paddle_width = 100
paddle_height = 20
paddle_x = window_width / 2 - paddle_width / 2
paddle_y = window_height - paddle_height - 10

# Kích thước và tọa độ của bóng
ball_radius = 10
ball_x = window_width / 2
ball_y = window_height / 2

# Khối gạch
brick_rows = 5
brick_cols = 8
brick_width = window_width // brick_cols
brick_height = 30
bricks = []

for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick_rect)
    bricks.append(brick_row)

# Điểm số
score = 0
font_style = pygame.font.SysFont(None, 35)

def score_display(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    game_window.blit(value, [0, 0])

def game_loop():
    global paddle_x, ball_x, ball_y, ball_speed, score

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle_x += paddle_speed

        # Giới hạn di chuyển của thanh ngang
        if paddle_x < 0:
            paddle_x = 0
        if paddle_x > window_width - paddle_width:
            paddle_x = window_width - paddle_width

        # Cập nhật vị trí của bóng
        ball_x += ball_speed[0]
        ball_y += ball_speed[1]

        # Kiểm tra va chạm giữa bóng và tường
        if ball_x - ball_radius < 0 or ball_x + ball_radius > window_width:
            ball_speed[0] = -ball_speed[0]
        if ball_y - ball_radius < 0:
            ball_speed[1] = -ball_speed[1]
        if ball_y + ball_radius > window_height:
            game_over = True

        # Kiểm tra va chạm giữa bóng và thanh ngang
        if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
            ball_speed[1] = -ball_speed[1]

        # Kiểm tra va chạm giữa bóng và khối gạch
        for row in bricks:
            for brick in row:
                if brick.collidepoint(ball_x, ball_y):
                    ball_speed[1] = -ball_speed[1]
                    row.remove(brick)
                    score += 1

        game_window.fill(white)
        pygame.draw.rect(game_window, black, [paddle_x, paddle_y, paddle_width, paddle_height])
        pygame.draw.circle(game_window, red, (ball_x, ball_y), ball_radius)

        for row in bricks:
            for brick in row:
                pygame.draw.rect(game_window, blue, brick)

        score_display(score)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
