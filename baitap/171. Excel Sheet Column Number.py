def titleToNumber(self, columnTitle):
        res = 0
        for char in columnTitle:
            # Chuyển ký tự thành số (A=1, B=2,...)
            value = ord(char) - ord('A') + 1
            # Công thức: kết quả cũ * 26 + giá trị mới
            res = res * 26 + value
        return res