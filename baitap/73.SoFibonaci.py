def fib(self, n):
    # Trường hợp cơ sở theo đề bài
        if n == 0: return 0
        if n == 1: return 1
        
        # Khởi tạo hai số đầu tiên
        a, b = 0, 1
        
        # Tính toán dần đến n
        for _ in range(2, n + 1):
            # Số tiếp theo bằng tổng hai số đứng trước
            a, b = b, a + b
            
        return b