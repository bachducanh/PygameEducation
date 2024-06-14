import pygame

pygame.init()

# Kích thước cửa sổ game
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pong')

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
paddle_width = 20
paddle_height = 100

paddle1_x = 30
paddle1_y = window_height / 2 - paddle_height / 2

paddle2_x = window_width - 30 - paddle_width
paddle2_y = window_height / 2 - paddle_height / 2

# Kích thước và tọa độ của bóng
ball_radius = 15
ball_x = window_width / 2
ball_y = window_height / 2

# Điểm số
score1 = 0
score2 = 0

font_style = pygame.font.SysFont(None, 35)

def score_display(score1, score2):
    value1 = font_style.render("Player 1: " + str(score1), True, black)
    value2 = font_style.render("Player 2: " + str(score2), True, black)
    game_window.blit(value1, [50, 10])
    game_window.blit(value2, [window_width - 200, 10])

def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_speed, score1, score2

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s]:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP]:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle2_y += paddle_speed

        # Giới hạn di chuyển của thanh ngang
        if paddle1_y < 0:
            paddle1_y = 0
        if paddle1_y > window_height - paddle_height:
            paddle1_y = window_height - paddle_height
        if paddle2_y < 0:
            paddle2_y = 0
        if paddle2_y > window_height - paddle_height:
            paddle2_y = window_height - paddle_height

        # Cập nhật vị trí của bóng
        ball_x += ball_speed[0]
        ball_y += ball_speed[1]

        # Kiểm tra va chạm giữa bóng và tường
        if ball_y - ball_radius < 0 or ball_y + ball_radius > window_height:
            ball_speed[1] = -ball_speed[1]

        # Kiểm tra va chạm giữa bóng và thanh ngang
        if paddle1_x < ball_x - ball_radius < paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_speed[0] = -ball_speed[0]
        if paddle2_x < ball_x + ball_radius < paddle2_x + paddle_width and paddle2_y < ball_y < paddle2_y + paddle_height:
            ball_speed[0] = -ball_speed[0]

        # Kiểm tra điểm số
        if ball_x - ball_radius < 0:
            score2 += 1
            ball_x = window_width / 2
            ball_y = window_height / 2
            ball_speed = [4, -4]
        if ball_x + ball_radius > window_width:
            score1 += 1
            ball_x = window_width / 2
            ball_y = window_height / 2
            ball_speed = [-4, 4]

        game_window.fill(white)
        pygame.draw.rect(game_window, black, [paddle1_x, paddle1_y, paddle_width, paddle_height])
        pygame.draw.rect(game_window, black, [paddle2_x, paddle2_y, paddle_width, paddle_height])
        pygame.draw.circle(game_window, red, (ball_x, ball_y), ball_radius)
        score_display(score1, score2)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
