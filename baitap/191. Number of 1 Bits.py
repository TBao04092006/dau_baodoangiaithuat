def hammingWeight(self, n):
        count = 0
        while n:
            # Mẹo: n & (n - 1) sẽ xóa đi bit 1 cuối cùng bên phải
            n &= (n - 1)
            count += 1
        return count
        