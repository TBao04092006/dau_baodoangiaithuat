def smallestRangeII(nums, k):
        nums.sort()
        n = len(nums)
        
        # Kết quả ban đầu khi chưa thay đổi gì (hoặc tất cả cùng cộng/trừ k)
        res = nums[n-1] - nums[0]
        
        # Duyệt qua các điểm ngắt i
        for i in range(n - 1):
            # Tìm giá trị lớn nhất và nhỏ nhất mới tại điểm ngắt i
            high = max(nums[n-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i+1] - k)
            
            # Cập nhật kết quả tối ưu nhất
            res = min(res, high - low)
            
        return res