def isAdditiveNumber(self, num):
        n = len(num)
        
        # Thử mọi tổ hợp của số thứ nhất (i) và số thứ hai (j)
        # i là vị trí kết thúc của số thứ nhất, j là vị trí kết thúc của số thứ hai
        for i in range(1, n):
            for j in range(i + 1, n):
                # Tách số thứ nhất và số thứ hai
                s1, s2 = num[:i], num[i:j]
                
                # Kiểm tra số 0 đứng đầu (leading zeros)
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                
                # Hàm đệ quy hoặc vòng lặp để kiểm tra các số còn lại
                if self.isValid(s1, s2, j, num):
                    return True
        return False

def isValid(self, num1_str, num2_str, start_idx, full_num):
        # Nếu đã đi đến cuối chuỗi, nghĩa là dãy này hợp lệ
        if start_idx == len(full_num):
            return True
        
        # Tính tổng của 2 số trước đó
        sum_val = int(num1_str) + int(num2_str)
        sum_str = str(sum_val)
        
        # Kiểm tra xem tổng này có khớp với phần tiếp theo trong chuỗi không
        if not full_num.startswith(sum_str, start_idx):
            return False
        
        # Nếu khớp, tiếp tục kiểm tra số kế tiếp (số thứ 2 trở thành số thứ 1, tổng trở thành số thứ 2)
        return self.isValid(num2_str, sum_str, start_idx + len(sum_str), full_num)