import math
def constructRectangle(area):
    # Bước 1: Bắt đầu từ căn bậc hai của diện tích
    w = int(math.sqrt(area))
        
    # Bước 2: Giảm w cho đến khi tìm được ước số của diện tích
    while area % w != 0:
        w -= 1
        
    # Bước 3: Tính L dựa trên W đã tìm được
    l = area // w