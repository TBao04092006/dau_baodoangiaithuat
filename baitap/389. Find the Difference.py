def findTheDifference(self, s, t):
        res = 0
        # XOR tất cả mã ASCII của các ký tự trong s và t
        for char in s + t:
            res ^= ord(char)
        
        # Chuyển mã ASCII kết quả ngược lại thành ký tự
        return chr(res)