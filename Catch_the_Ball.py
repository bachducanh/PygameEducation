import pygame
import random

pygame.init()

# Kích thước cửa sổ game
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Catch the Ball')

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Đồng hồ
clock = pygame.time.Clock()
ball_speed = 5
paddle_speed = 10

# Tọa độ và kích thước của giỏ
paddle_width = 100
paddle_height = 20
paddle_x = window_width / 2 - paddle_width / 2
paddle_y = window_height - paddle_height - 10

# Kích thước và tọa độ của bóng
ball_radius = 15
ball_x = random.randint(ball_radius, window_width - ball_radius)
ball_y = 0

# Điểm số
score = 0

font_style = pygame.font.SysFont(None, 35)

def score_display(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    game_window.blit(value, [0, 0])

def game_loop():
    global paddle_x, ball_x, ball_y, score

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

        # Giới hạn di chuyển của giỏ
        if paddle_x < 0:
            paddle_x = 0
        if paddle_x > window_width - paddle_width:
            paddle_x = window_width - paddle_width

        # Cập nhật vị trí của bóng
        ball_y += ball_speed

        # Kiểm tra va chạm giữa bóng và giỏ
        if ball_y + ball_radius > paddle_y:
            if paddle_x < ball_x < paddle_x + paddle_width:
                score += 1
                ball_x = random.randint(ball_radius, window_width - ball_radius)
                ball_y = 0
            else:
                game_over = True

        if ball_y > window_height:
            game_over = True

        game_window.fill(white)
        pygame.draw.rect(game_window, black, [paddle_x, paddle_y, paddle_width, paddle_height])
        pygame.draw.circle(game_window, red, (ball_x, ball_y), ball_radius)
        score_display(score)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()
