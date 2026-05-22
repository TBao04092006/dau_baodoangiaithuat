def divide(self, dividend, divisor):
        # Xử lý trường hợp tràn số (overflow) đặc biệt của số nguyên 32-bit
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Xác định dấu của kết quả
        negative = (dividend < 0) != (divisor < 0)
        
        # Làm việc với số dương cho đơn giản
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # Dùng vòng lặp trừ dần theo cấp số nhân (dịch bit) để tối ưu thời gian
        while a >= b:
            temp, i = b, 1
            while a >= (temp << 1):
                temp <<= 1
                i <<= 1
            a -= temp
            res += i
            
        return -res if negative else res