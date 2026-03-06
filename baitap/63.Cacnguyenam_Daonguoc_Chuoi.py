def reverseVowels(self, s):
        nguyen_am = set("aeiouAEIOU")
        s = list(s) # Chuyển chuỗi thành danh sách để có thể sửa đổi
        trai, phai = 0, len(s) - 1
        
        while trai < phai:
            # Tìm nguyên âm từ bên trái
            while trai < phai and s[trai] not in nguyen_am:
                trai += 1
            # Tìm nguyên âm từ bên phải
            while trai < phai and s[phai] not in nguyen_am:
                phai -= 1
            
            # Hoán đổi hai nguyên âm tìm được
            s[trai], s[phai] = s[phai], s[trai]
            
            # Tiếp tục di chuyển
            trai += 1
            phai -= 1
            
        return "".join(s)