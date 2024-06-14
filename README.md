Khởi tạo Pygame: pygame.init() khởi tạo các mô-đun của Pygame.
Thiết lập cửa sổ:
window_width và window_height đặt kích thước cửa sổ game.
game_window tạo cửa sổ game với kích thước đã cho.
pygame.display.set_caption('Snake Game') đặt tiêu đề cho cửa sổ.
Đồng hồ và tốc độ:
clock để điều khiển tốc độ khung hình của trò chơi.
block_size đặt kích thước của mỗi ô vuông (mỗi đoạn của rắn).
snake_speed đặt tốc độ di chuyển của rắn.
Font chữ: font_style tạo font chữ cho điểm số hiển thị.
score_display(score):

Hiển thị điểm số hiện tại của người chơi trên màn hình.
font_style.render tạo hình ảnh chứa điểm số với màu đen (black).
game_window.blit vẽ hình ảnh điểm số lên cửa sổ game tại vị trí [0, 0].
our_snake(block_size, snake_list):

Vẽ các đoạn của con rắn lên màn hình.
snake_list chứa tọa độ của các đoạn rắn.
pygame.draw.rect vẽ mỗi đoạn rắn với kích thước block_size.
message(msg, color):

Hiển thị thông báo khi game kết thúc.
font_style.render tạo hình ảnh chứa thông báo với màu đã cho (color).
game_window.blit vẽ hình ảnh thông báo lên cửa sổ game tại vị trí [window_width / 6, window_height / 3].

Khởi tạo các biến:
game_over và game_close để kiểm soát trạng thái của trò chơi.
x1 và y1 là tọa độ ban đầu của rắn, được đặt ở giữa cửa sổ game.
x1_change và y1_change là biến để kiểm soát sự thay đổi vị trí của rắn.
snake_list lưu trữ các tọa độ của các đoạn rắn.
length_of_snake lưu trữ độ dài của rắn.
foodx và foody là tọa độ của thức ăn, được tạo ngẫu nhiên.
score lưu trữ điểm số của người chơi.
direction để theo dõi hướng di chuyển hiện tại của rắn.
Kiểm tra trạng thái game:
while not game_over: bắt đầu vòng lặp chính của game.
while game_close: hiển thị thông báo khi game kết thúc và chờ người chơi chọn tiếp tục hoặc thoát.
pygame.display.update() cập nhật màn hình.
pygame.event.get() lấy các sự kiện từ hàng đợi sự kiện.
Nếu người chơi nhấn phím Q, game_over được đặt thành True để thoát khỏi vòng lặp chính.
Nếu người chơi nhấn phím C, hàm game_loop() được gọi lại để bắt đầu lại trò chơi.
Xử lý sự kiện:
if event.type == pygame.QUIT: kiểm tra xem người chơi có đóng cửa sổ game không.
if event.type == pygame.KEYDOWN: kiểm tra các phím được nhấn.
Các điều kiện kiểm tra để đảm bảo rắn không thể di chuyển ngược lại hướng hiện tại (ví dụ: nếu rắn đang di chuyển sang phải, nó không thể di chuyển sang trái ngay lập tức).
Cập nhật vị trí:
x1 += x1_change và y1 += y1_change cập nhật tọa độ của rắn dựa trên hướng di chuyển.
Xử lý va chạm với tường:
Nếu rắn đi qua cạnh phải, nó sẽ xuất hiện ở cạnh trái và ngược lại.
Nếu rắn đi qua cạnh trên, nó sẽ xuất hiện ở cạnh dưới và ngược lại.
Vẽ rắn và thức ăn:
game_window.fill(white) làm sạch màn hình.
pygame.draw.rect vẽ thức ăn.
Cập nhật tọa độ của đầu rắn và thêm vào snake_list.
Xóa đoạn cuối của rắn nếu độ dài hiện tại vượt quá length_of_snake.
Kiểm tra va chạm với chính mình:
Nếu đầu rắn va chạm với bất kỳ đoạn nào trong thân rắn, game_close được đặt thành True.
Hiển thị rắn và điểm số:
our_snake(block_size, snake_list) vẽ rắn.
score_display(score) hiển thị điểm số hiện tại.
pygame.display.update() cập nhật màn hình.
Kiểm tra va chạm với thức ăn:
Nếu đầu rắn nằm trên tọa độ của thức ăn, tọa độ thức ăn mới được tạo ngẫu nhiên.
length_of_snake và score được tăng lên.
Điều khiển tốc độ:
clock.tick(snake_speed) điều khiển tốc độ khung hình của trò chơi.
Thoát trò chơi:
pygame.quit() thoát khỏi Pygame.
quit() thoát khỏi chương trình Python.
