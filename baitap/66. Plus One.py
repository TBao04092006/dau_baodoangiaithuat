def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # Nếu tất cả các số đều là 9 (vd: 99 -> 100)
        return [1] + digits