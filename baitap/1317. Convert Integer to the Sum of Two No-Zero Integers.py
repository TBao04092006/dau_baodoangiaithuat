def getNoZeroIntegers(self, n):
        def has_zero(num):
            # Kiểm tra xem số có chứa chữ số '0' không bằng cách chuyển sang chuỗi
            return '0' in str(num)
        
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]