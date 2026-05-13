def removePalindromeSub(self, s):
        if not s:
            return 0
        
        # Kiểm tra chuỗi đối xứng bằng cách đảo ngược chuỗi
        if s == s[::-1]:
            return 1
        
        # Mọi trường hợp còn lại đều là 2 bước
        return 2