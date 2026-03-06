def reverseBits(self, n):
        res = 0
        for i in range(32):
            # Dịch res sang trái để nhường chỗ cho bit mới
            res = (res << 1) | (n & 1)
            # Dịch n sang phải để xét bit tiếp theo
            n >>= 1
        return res