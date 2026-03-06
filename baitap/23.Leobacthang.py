def climbStairs(self, n):
        if n <= 2: return n
        
        # cach_1: số cách lên bậc hiện tại - 1
        # cach_2: số cách lên bậc hiện tại - 2
        cach_2, cach_1 = 1, 2
        
        for i in range(3, n + 1):
            tong_cach = cach_1 + cach_2
            # Cập nhật lại cho bước tiếp theo
            cach_2 = cach_1
            cach_1 = tong_cach
            
        return cach_1