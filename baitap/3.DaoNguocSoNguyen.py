def reverse(self, x):
        # Xác định dấu của số (1 là dương, -1 là âm)
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            # Lấy chữ số cuối
            digit = x % 10
            # Đưa chữ số đó vào số đã đảo ngược
            reversed_num = reversed_num * 10 + digit
            # Loại bỏ chữ số cuối của x
            x //= 10
            
        # Áp dụng lại dấu ban đầu
        result = sign * reversed_num
        
        # Kiểm tra tràn số (giới hạn 32-bit: -2^31 đến 2^31 - 1)
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result