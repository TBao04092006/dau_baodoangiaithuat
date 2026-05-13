def addStrings(self, num1, num2):
        res = []
        carry = 0
        # Khởi tạo con trỏ ở cuối mỗi chuỗi
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        # Lặp cho đến khi hết cả hai chuỗi và không còn số nhớ
        while p1 >= 0 or p2 >= 0 or carry:
            # Lấy giá trị số tại vị trí p1, p2 (nếu hết chuỗi thì coi là 0)
            digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            # Tính tổng và biến nhớ
            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            # Dịch con trỏ sang trái
            p1 -= 1
            p2 -= 1
            
        # Vì ta append vào cuối nên kết quả đang bị ngược, cần đảo lại
        return "".join(res[::-1])
        