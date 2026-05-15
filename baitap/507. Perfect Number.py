import math
def checkPerfectNumber(self, num):
        # Số hoàn hảo phải là số dương và không thể là 1 
        # (vì ước của 1 ngoại trừ chính nó là rỗng, tổng = 0)
        if num <= 1:
            return False
            
        total_sum = 1 # 1 luôn là ước của mọi số dương > 1
        sqrt_num = int(math.sqrt(num))
        
        # Duyệt từ 2 đến căn bậc hai của num
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                total_sum += i
                # Nếu i*i không phải là num (tránh cộng trùng số giống nhau)
                if i * i != num:
                    total_sum += num // i
                    
        return total_sum == num