def isPowerOfTwo(self, n):
        # Lũy thừa của 2 phải là số dương
        # Và n & (n - 1) phải bằng 0
        return n > 0 and (n & (n - 1)) == 0