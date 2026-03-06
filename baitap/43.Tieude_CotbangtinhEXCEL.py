def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 0:
            columnNumber -= 1 # Điều chỉnh về 0-indexed
            res = chr(columnNumber % 26 + ord('A')) + res
            columnNumber //= 26
        return res
            