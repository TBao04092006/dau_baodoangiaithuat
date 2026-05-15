def subtractProductAndSum(self, n):
        product_val = 1
        sum_val = 0
        
        while n > 0:
            # Lấy chữ số cuối cùng
            digit = n % 10
            
            # Cập nhật tích và tổng
            product_val *= digit
            sum_val += digit
            
            # Loại bỏ chữ số cuối cùng để xét tiếp
            n //= 10
            
        return product_val - sum_val