def isSubsequence(s, t):
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            # Nếu ký tự khớp, tiến con trỏ trên chuỗi s
            if s[i] == t[j]:
                i += 1
            # Luôn tiến con trỏ trên chuỗi t
            j += 1
            
        # Nếu i bằng độ dài của s, nghĩa là đã tìm thấy toàn bộ dãy con
        return i == len(s)
        