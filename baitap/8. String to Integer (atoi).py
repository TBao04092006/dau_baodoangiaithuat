def myAtoi(self, s):
        # Bước 1: Loại bỏ khoảng trắng ở đầu chuỗi
        s = s.lstrip()
        if not s:
            return 0
        
        # Bước 2: Xác định dấu
        sign = 1
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Bước 3: Đọc các chữ số
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Áp dụng dấu
        res *= sign
        
        # Bước 4: Làm tròn trong phạm vi số nguyên 32-bit có dấu
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res