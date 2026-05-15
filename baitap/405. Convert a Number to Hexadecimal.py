def toHex(self, num):
        if num == 0: return "0"
        
        # Ánh xạ giá trị 0-15 sang ký tự hex
        hex_map = "0123456789abcdef"
        res = ""
        
        # Xử lý số nguyên 32-bit (ép kiểu số âm về số bù hai trong Python)
        if num < 0:
            num = num + (2**32)
            
        while num > 0:
            # Lấy 4 bit cuối cùng (num % 16)
            digit = num & 15 
            res = hex_map[digit] + res
            # Dịch phải 4 bit để xử lý nhóm tiếp theo
            num >>= 4
            
        return res
        