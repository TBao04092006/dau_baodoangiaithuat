def isPalindrome(self, s):
        # 1. Làm sạch chuỗi: chỉ giữ lại chữ cái và số, chuyển thành chữ thường
        # Chúng ta dùng hàm isalnum() để kiểm tra ký tự có phải chữ hoặc số không
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. So sánh chuỗi đã làm sạch với chuỗi đảo ngược của nó [::-1]
        return clean_s == clean_s[::-1]