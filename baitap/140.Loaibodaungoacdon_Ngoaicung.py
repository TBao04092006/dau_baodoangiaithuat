def removeOuterParentheses(self, s):
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # Nếu đã có ít nhất 1 dấu ngoặc đang mở, 
                # thì dấu '(' này nằm bên trong
                if opened > 0:
                    res.append(char)
                opened += 1
            else: # char == ')'
                opened -= 1
                # Nếu sau khi đóng, vẫn còn dấu ngoặc đang mở,
                # thì dấu ')' này nằm bên trong
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)
        