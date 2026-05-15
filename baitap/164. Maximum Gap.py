def maximumGap(self, nums):
        if len(nums) < 2: return 0
        
        hi, lo, n = max(nums), min(nums), len(nums)
        if hi == lo: return 0
        
        # Kích thước và số lượng thùng
        bsize = max(1, (hi - lo) // (n - 1))
        num_buckets = (hi - lo) // bsize + 1
        buckets = [[None, None] for _ in range(num_buckets)]
        
        # Bước 1: Đưa các số vào thùng (chỉ giữ min/max của mỗi thùng)
        for x in nums:
            b = buckets[(x - lo) // bsize]
            b[0] = x if b[0] is None else min(b[0], x)
            b[1] = x if b[1] is None else max(b[1], x)
            
        # Bước 2: So sánh khoảng cách giữa các thùng
        max_gap = 0
        prev_max = lo
        for b_min, b_max in buckets:
            if b_min is None: continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
            
        return max_gap