def longestPalindrome(self, s):
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1  # Lấy phần chẵn của số lẻ
                has_odd = True       # Đánh dấu có ký tự lẻ
        
        # Nếu có ít nhất một ký tự lẻ, ta cộng thêm 1 cho vị trí ở giữa
        return length + 1 if has_odd else length
        