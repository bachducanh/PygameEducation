import pygame

pygame.init()

# Kích thước cửa sổ game
window_width = 300
window_height = 300
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tic-Tac-Toe')

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Đồng hồ
clock = pygame.time.Clock()

# Bàn cờ
board = [[None]*3, [None]*3, [None]*3]

# Biến kiểm soát lượt chơi
current_player = "X"

def draw_board():
    for row in range(1, 3):
        pygame.draw.line(game_window, black, (0, row*100), (300, row*100), 2)
        pygame.draw.line(game_window, black, (row*100, 0), (row*100, 300), 2)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(game_window, red, (col*100+20, row*100+20), (col*100+80, row*100+80), 2)
                pygame.draw.line(game_window, red, (col*100+80, row*100+20), (col*100+20, row*100+80), 2)
            elif board[row][col] == "O":
                pygame.draw.circle(game_window, blue, (col*100+50, row*100+50), 40, 2)

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def game_loop():
    global current_player

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // 100
                row = y // 100

                if board[row][col] is None:
                    board[row][col] = current_player
                    winner = check_winner()
                    if winner is not None:
                        print(f"Player {winner} wins!")
                        game_over = True
                    current_player = "O" if current_player == "X" else "X"

        game_window.fill(white)
        draw_board()
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()
