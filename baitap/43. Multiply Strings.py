def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Mảng chứa kết quả có độ dài tối đa là tổng độ dài 2 chuỗi
        res = [0] * (len(num1) + len(num2))
        
        # Đảo ngược chuỗi để nhân từ hàng đơn vị lên
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Nhân hai chữ số (chuyển từng ký tự sang số bằng ord)
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                multi = digit1 * digit2
                
                # Cộng vào vị trí tương ứng trong mảng kết quả
                res[i + j] += multi
                # Xử lý nhớ (carry)
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        
        # Loại bỏ các số 0 thừa ở cuối (do ta đảo ngược mảng)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        # Đảo ngược lại và chuyển thành chuỗi
        return "".join(map(str, res[::-1]))