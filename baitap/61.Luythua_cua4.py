def isPowerOfFour(self, n):
        # 1. n phải dương
        # 2. n phải là lũy thừa của 2: n & (n - 1) == 0
        # 3. Bit 1 phải nằm ở vị trí lẻ: n % 3 == 1
        # (Vì 4^x - 1 luôn chia hết cho 3)
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
        