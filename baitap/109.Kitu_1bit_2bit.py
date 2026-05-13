def isOneBitCharacter(bits):
        i = 0
        n = len(bits)
        # Duyệt cho đến trước phần tử cuối cùng
        while i < n - 1:
            if bits[i] == 1:
                # Nếu là 1, đây là ký tự 2-bit, nhảy 2 bước
                i += 2
            else:
                # Nếu là 0, đây là ký tự 1-bit, nhảy 1 bước
                i += 1
        
        # Nếu i dừng lại đúng ở n-1, thì bit cuối là ký tự 1-bit
        return i == n - 1
        