def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        for n in range(left, right + 1):
            # Logic toán học của bạn nằm ở đây
            temp = n
            is_valid = True
            
            while temp > 0:
                digit = temp % 10
                # Kiểm tra số 0 hoặc không chia hết
                if digit == 0 or n % digit != 0:
                    is_valid = False
                    break
                temp //= 10
            
            if is_valid:
                result.append(n)
                
        return result